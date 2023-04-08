from __future__ import annotations

import logging
import os
from typing import Optional, Sequence

import jinja2
from jinja2.ext import Extension, InternationalizationExtension

from mkdocs.config.base import ValidationError

try:
    from babel.core import Locale, UnknownLocaleError
    from babel.support import NullTranslations, Translations

    has_babel = True
except ImportError:  # pragma: no cover
    from mkdocs.utils.babel_stub import Locale, UnknownLocaleError

    has_babel = False


log = logging.getLogger(__name__)
base_path = os.path.dirname(os.path.abspath(__file__))


class NoBabelExtension(InternationalizationExtension):  # pragma: no cover
    def __init__(self, environment):
        Extension.__init__(self, environment)
        environment.extend(
            install_null_translations=self._install_null,
            newstyle_gettext=False,
        )


def parse_locale(locale) -> Locale:
    try:
        return Locale.parse(locale, sep='_')
    except (ValueError, UnknownLocaleError, TypeError) as e:
        raise ValidationError(f'Invalid value for locale: {str(e)}')


def install_translations(
    env: jinja2.Environment, locale: Locale, theme_dirs: Sequence[str]
) -> None:
    if has_babel:
        env.add_extension('jinja2.ext.i18n')
        translations = _get_merged_translations(theme_dirs, 'locales', locale)
        if translations is not None:
            env.install_gettext_translations(translations)
        else:
            env.install_null_translations()
            if locale.language != 'en':
                log.warning(
                    f"No translations could be found for the locale '{locale}'. "
                    'Defaulting to English.'
                )
    else:  # pragma: no cover
        # no babel installed, add dummy support for trans/endtrans blocks
        env.add_extension(NoBabelExtension)
        env.install_null_translations()


def _get_merged_translations(
    theme_dirs: Sequence[str], locales_dir: str, locale: Locale
) -> Optional[Translations]:
    merged_translations: Optional[Translations] = None

    log.debug(f"Looking for translations for locale '{locale}'")
    if locale.territory:
        locale_str = f"{locale.language}_{locale.territory}"
    else:
        locale_str = locale.language
    for theme_dir in reversed(theme_dirs):
        dirname = os.path.join(theme_dir, locales_dir)
        translations = Translations.load(dirname, [locale_str])

        if type(translations) is NullTranslations:
            log.debug(f"No translations found here: '{dirname}'")
            continue

        log.debug(f"Translations found here: '{dirname}'")
        if merged_translations is None:
            merged_translations = translations
        else:
            merged_translations.merge(translations)

    return merged_translations

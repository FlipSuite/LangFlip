"""TODO: Manages the translation of transcribed text to the target language."""
import argostranslate.package
import argostranslate.translate

def translate(from_code, to_code, text):

    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())

    # Translate
    translatedText = argostranslate.translate.translate(text, from_code, to_code)
    print(translatedText)
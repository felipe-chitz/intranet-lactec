from lactec.intranet import PACKAGE_NAME
from zope.schema.vocabulary import SimpleVocabulary

import pytest


class TestVocabEstados:
    name = f"{PACKAGE_NAME}.vocabulary.estados"

    @pytest.fixture(autouse=True)
    def _setup(self, get_vocabulary, portal):
        """Configura o vocabulário para os testes.

        get_vocabulary: Fixture para obter o vocabulário registrado.
                        Definida em pytest-plone.
        portal: Fixture do portal Plone.
                Definida em pytest-plone.
        """
        self.vocab = get_vocabulary(self.name, portal)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, SimpleVocabulary)

    @pytest.mark.parametrize(
        "token, title",
        [
            ("PR", "Paraná"),
            ("SP", "São Paulo"),
            ("MT", "Mato Grosso"),
        ],
    )
    def test_voc(self, token: str, title: str):
        """Verifica se o token existe no vocabulário."""
        term = self.vocab.getTermByToken(token)

        assert term is not None
        assert term.token == token
        assert term.title == title

    def test_voc_len(self):
        """Verifica o total de estados no vocabulário"""
        assert len(self.vocab) == 27

from onmt.modules.Transformer import \
   TransformerEncoder, TransformerDecoder
from onmt.modules.Embeddings import Embeddings, PositionalEncoding
from onmt.modules.Generator import Generator
from onmt.Models import NMTModel

# For flake8 compatibility.
__all__ = [NMTModel, PositionalEncoding, TransformerEncoder, TransformerDecoder, Embeddings, Generator]

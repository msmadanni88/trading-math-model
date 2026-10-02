"""probcast - self-learning online candle generator."""
import os

# The matrices here are small: BLAS worker threads only add overhead (and can
# stall badly on shared cloud runners). Must be set before numpy is imported.
for _v in ("OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

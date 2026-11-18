import random
import time

from azure.core.exceptions import HttpResponseError


def with_retry(func, *args, max_attempts=5, base_delay=1.0, **kwargs):
    """Appelle func ; en cas d'erreur 429 ou 5xx, réessaie avec attente exponentielle."""
    for attempt in range(1, max_attempts + 1):
        try:
            return func(*args, **kwargs)
        except HttpResponseError as e:
            code = getattr(e, "status_code", None)
            retryable = code == 429 or (code is not None and code >= 500)
            if not retryable or attempt == max_attempts:
                raise
            delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5)
            print(f"Erreur {code}, nouvel essai {attempt}/{max_attempts - 1} dans {delay:.1f}s")
            time.sleep(delay)
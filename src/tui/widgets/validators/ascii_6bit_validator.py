from textual.validation import Validator, ValidationResult

from converter.internal.ascii_6bit import ASCII_6BIT_MAP


class ASCII6bitValidator(Validator):
    def validate(self, value: str) -> ValidationResult:
        for ch in value:
            if ch not in ASCII_6BIT_MAP:
                return self.failure(
                    f"Symbol '{ch}' can't appear in ASCII 6bit encoding. Allowed: '{ASCII_6BIT_MAP}'"
                )

        return self.success()

from textual.validation import Validator, ValidationResult

from converter.internal.bcd import BCD_TO_STR_MAP


class BcdValidator(Validator):
    def validate(self, value: str) -> ValidationResult:
        for ch in value:
            if ch not in BCD_TO_STR_MAP:
                return self.failure(
                    f"Symbol '{ch}' can't appear in BCD+ encoding. Allowed: '{BCD_TO_STR_MAP}'"
                )

        return self.success()

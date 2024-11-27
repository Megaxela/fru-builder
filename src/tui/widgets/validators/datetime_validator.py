from datetime import datetime, timedelta

from textual.validation import Validator, ValidationResult

from converter.internal.bcd import BCD_TO_STR_MAP

MIN_DATE = datetime(1996, 1, 1)
MAX_DATE = MIN_DATE + timedelta(minutes=0xFF**3)


class DateTimeValidator(Validator):
    def validate(self, value: str) -> ValidationResult:
        if not value:
            return self.success()

        try:
            parsed_date = datetime.strptime(value, "%d-%m-%Y %H:%M")
        except ValueError as e:
            return self.failure(f"Invalid datetime format: {str(e)}")

        if parsed_date < MIN_DATE:
            return self.failure(
                f"Date must be later than {MIN_DATE.strftime('%d-%m-%Y %H:%M')}"
            )

        if parsed_date > MAX_DATE:
            return self.failure(
                f"Date must be earlier than {MAX_DATE.strftime('%d-%m-%Y %H:%M')}"
            )

        return self.success()

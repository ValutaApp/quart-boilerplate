ERROR_MESSAGES = {
    10001: "Registrations are disabled",
    10011: "Missing token in 'Authorization' Header",
    10012: "Invalid token in 'Authorization' Header",
    10013: "Missing token",
    10014: "Invalid token"
}


class APIError(Exception):
    status_code = 500

    def _get_error_msg(self, error_code):
        try:
            if error_code is not None:
                return ERROR_MESSAGES.get(error_code) or self.args[0]
        except IndexError:
            pass

        return repr(self)

    @property
    def message(self):
        try:
            message = self.args[0]

            return self._get_error_msg(message) if isinstance(message, int) else message
        except IndexError:
            return self._get_error_msg(getattr(self, "error_code", None))

    @property
    def json(self):
        args = getattr(self, "args", None)
        return args[1] if args and len(args) > 1 else None


class BadRequest(APIError):
    status_code = 400


class Unauthorized(APIError):
    status_code = 401


class Forbidden(APIError):
    status_code = 403


class NotFound(APIError):
    status_code = 404


class RegistrationsDisabled(BadRequest):
    error_code = 10001


class TooManyUsers(BadRequest):
    error_code = 10002


class EmailExists(BadRequest):
    error_code = 10004


class PasswordMismatch(Unauthorized):
    error_code = 10005


class InvalidPassword(Unauthorized):
    error_code = 10006


class MissingToken(Unauthorized):
    error_code = 10010


class TokenInvalidUserID(Unauthorized):
    error_code = 10011


class InvalidToken(Forbidden):
    error_code = 10012


class InvalidSession(BadRequest):
    error_code = 10013

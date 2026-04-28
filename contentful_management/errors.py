"""
contentful_management.errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Error classes.

API reference: https://www.contentful.com/developers/docs/references/content-delivery-api/#/introduction/errors

:copyright: (c) 2018 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class HTTPError(Exception):
    """
    Base HTTP error class.
    """

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code

        message = self._best_available_message(response)
        super(HTTPError, self).__init__(message)

    def _default_error_message(self):
        pass

    def _handle_details(self, details):
        pass

    def _has_additional_error_info(self):
        pass

    def _additional_error_info(self):
        pass

    def _best_available_message(self, response):
        pass


class BadRequestError(HTTPError):
    """
    400
    """

    def _default_error_message(self):
        pass

    def _handle_details(self, details):
        pass


class UnauthorizedError(HTTPError):
    """
    401
    """

    def _default_error_message(self):
        pass


class AccessDeniedError(HTTPError):
    """
    403
    """

    def _default_error_message(self):
        pass

    def _handle_details(self, details):
        pass


class NotFoundError(HTTPError):
    """
    404
    """

    def _default_error_message(self):
        pass

    def _handle_details(self, details):
        pass


class VersionMismatchError(HTTPError):
    """
    409
    """
    def _default_error_message(self):
        pass


class UnprocessableEntityError(HTTPError):
    """
    422
    """
    def _default_error_message(self):
        pass

    def _handle_error(self, error):
        pass

    def _handle_details(self, details):
        pass


class RateLimitExceededError(HTTPError):
    """
    429
    """

    RATE_LIMIT_RESET_HEADER_KEY = 'x-contentful-ratelimit-reset'

    def _has_reset_time(self):
        pass

    def reset_time(self):
        """Returns the reset time in seconds until next available request."""
        pass

    def _has_additional_error_info(self):
        pass

    def _additional_error_info(self):
        pass

    def _default_error_message(self):
        pass


class ServerError(HTTPError):
    """
    500
    """

    def _default_error_message(self):
        pass


class BadGatewayError(HTTPError):
    """
    502
    """

    def _default_error_message(self):
        pass


class ServiceUnavailableError(HTTPError):
    """
    503
    """

    def _default_error_message(self):
        pass


def get_error(response):
    """
    Gets Error by HTTP status code.
    """

    errors = {
        400: BadRequestError,
        401: UnauthorizedError,
        403: AccessDeniedError,
        404: NotFoundError,
        409: VersionMismatchError,
        422: UnprocessableEntityError,
        429: RateLimitExceededError,
        500: ServerError,
        502: BadGatewayError,
        503: ServiceUnavailableError
    }

    error_class = HTTPError
    if response.status_code in errors:
        error_class = errors[response.status_code]

    return error_class(response)

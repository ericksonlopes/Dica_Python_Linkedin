class PageNotFound(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    try:
        raise PageNotFound('Page not found')
    except PageNotFound as e:
        print(e)

    # [Output]
    # Page not found

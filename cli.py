from argparse import Action, ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

    def create_parser():
        parser = ArgumentParser(description=""" back up postgres database locally and maybe to aws s3 if im not lazy""")
        parser.add_argument("url", help ="URL of database to backup")
        parser.add_argument("--driver",
                help = "how and where to store backup",
                nargs =2,
                action = DriverAction,
                required = True)
        return parser


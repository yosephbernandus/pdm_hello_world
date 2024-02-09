from argparse import ArgumentParser
from pdm_hello_world.hello_world import hello

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-name', dest='name', default='Jhon Doe')
    args = parser.parse_args()

    print(hello(args.name))

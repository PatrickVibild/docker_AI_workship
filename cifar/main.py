import os


def main():
    try:
        app = os.environ['SCRIPT']
    except:
        raise Exception("Environment variable SCRIPT not define.")
    exec(open('/code/cifar/' + app).read())


if __name__ == '__main__':
    main()

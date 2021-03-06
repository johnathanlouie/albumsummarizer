from argparse import ArgumentParser, Namespace

import aaa
from core import modelbuilder


def proc_args() -> Namespace:
    """
    Parses program arguments.
    """
    parser = ArgumentParser(description='Deep learning section of the album summarizer.')
    parser.add_argument('mode', help='', choices=['train', 'predict'])
    parser.add_argument('architecture', help='', choices=modelbuilder.ModelBuilder.ARCHITECTURES.keys())
    parser.add_argument('dataset', help='', choices=modelbuilder.ModelBuilder.DATASETS.keys())
    parser.add_argument('split', help='', type=int)
    parser.add_argument('loss', help='', type=int)
    parser.add_argument('optimizer', help='', type=int)
    parser.add_argument('metric', help='', type=int)
    parser.add_argument('-e', '--epochs', help='', type=int, default=100)
    parser.add_argument('-p', '--patience', help='', type=int, default=5)
    args = parser.parse_args()
    return args


def main() -> None:
    """
    Starts the program.
    """
    args = proc_args()
    mode = args.mode
    epochs = args.epochs
    patience = args.patience
    x = modelbuilder.ModelBuilder.create_split(
        args.architecture,
        args.dataset,
        args.split,
        args.loss,
        args.optimizer,
        args.metric
    )
    if mode == 'train':
        x.train(epochs, patience)
    elif mode == 'validate':
        x.validate(epochs, patience)
    elif mode == 'test':
        x.test(epochs, patience)
    elif mode == 'predict':
        raise NotImplementedError
        # x.predict(epochs, patience)
    else:
        raise Exception
    return


if __name__ == '__main__':
    main()

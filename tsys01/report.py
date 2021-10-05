#!/usr/bin/python3

import matplotlib.pyplot as plt

def generate_figures(log):
    footer = f'tsys01 test report'

    f, spec = log.figure(height_ratios=[1,1], suptitle=f'tsys01 data', footer=footer)

    plt.subplot(spec[0,:])
    log.data.temperature.pplot()

    plt.subplot(spec[1,:])

    # todo check if log.error exists
    try:
        log.error.ttable(rl=True)
    except:
        pass

def main():
    from llog import LLogReader
    from matplotlib.backends.backend_pdf import PdfPages
    from pathlib import Path

    parser = LLogReader.create_default_parser(__file__, 'tsys01')
    args = parser.parse_args()

    log = LLogReader(args.input, args.meta)

    generate_figures(log)

    if args.output:
        if Path(args.output).exists():
            print(f'WARN {args.output} exists! skipping ..')
        else:
            with PdfPages(args.output) as pdf:
                [pdf.savefig(n) for n in plt.get_fignums()]

    if args.show:
        plt.show()

if __name__ == '__main__':
    main()

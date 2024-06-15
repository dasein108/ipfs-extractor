import sys
import argparse
from data.utils.files import read_file
from data.source.ipfs_gateway import read_text_from_cid
from transform import create_summary, extract_scored_keywords

#
# text_content = read_file("samples/QmXkEnWAXjtQVxv3GFg4Y5e6pbXT8Jm2RaQK7DEBtFZTKj")
#
# summary_long, summary_short = create_summary(text_content)
# print("=== SUMMARY LONG ===")
# print(summary_long)
# print("\r\n=== SUMMARY SHORT ===")
# print(summary_short)
#
# scored_keywords = extract_scored_keywords(text_content)
# keyword_items = [f'{i}. {e[0]} ({round(e[1], 2)})' for i, e in enumerate(scored_keywords)]
#
# print("\r\n=== KEYWORDS ===")
# print("\r\n".join(keyword_items))


def main():
    parser = argparse.ArgumentParser(description='Perform Named Entity Recognition and '
                                                 'Summarization of text content from a file or IPFS CID.')

    # Add arguments
    parser.add_argument('-f', '--file', type=str, help='Filename to process')
    parser.add_argument('-c', '--cid', type=str, help='IPFS CID to process')
    parser.add_argument('--ner', action='store_true', help='Perform Named Entity Recognition(default: enabled)')
    parser.add_argument('--sum', action='store_true', help='Perform Summarization(default: enabled)')

    parser.set_defaults(ner=True, sum=True)

    # Parse the arguments
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        exit()

    if not args.file and not args.cid:
        parser.error('--file or --cid must be specified')

    text_content = ''

    # Use the arguments
    if args.file:
        print(f'processing {args.file} ...')
        text_content = read_file(args.file)

    if args.cid:
        print(f'processing {args.cid} ...')
        text_content = read_text_from_cid(args.cid)

    if args.ner:
        scored_keywords = extract_scored_keywords(text_content)
        keyword_items = [f'{i}. {e[0]} ({round(e[1], 2)})' for i, e in enumerate(scored_keywords)]

        print("\r\n=== KEYWORDS ===")
        print("\r\n".join(keyword_items))
    if args.sum:
        summary_long, summary_short = create_summary(text_content)
        print("=== SUMMARY LONG ===")
        print(summary_long)
        print("\r\n=== SUMMARY SHORT ===")
        print(summary_short)


if __name__ == '__main__':
    main()

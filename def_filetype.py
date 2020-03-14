import filetype

def main():
    kind = filetype.guess('savedrecs.txt')
    if kind is None:
        print('Cannot guess file type !')
        return

    print('File Extension: %s' %kind.extension)
    print('File MIME type: %s' %kind.mime)

if __name__ == '__main__':
    main()
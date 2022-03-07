import tarfile
import email

#FILENAME = "sampleEmails.tar.gz"

# https://stackoverflow.com/questions/12903893/python-imap-utf-8q-in-subject-string
def decode_mime_words(s):
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(word, bytes) else word
        for word, encoding in email.header.decode_header(s))

# Input - filename - Filename of tar.gz of .msg files
# Returns - out - array of email message objects
def parse_file(filename):
    out = []
    tar = tarfile.open(filename)
    for member in tar.getmembers():
        f = tar.extractfile(member)
        if f is not None:
            msg = email.message_from_bytes(f.read())
            out.append(msg)
    return out
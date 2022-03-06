import tarfile
import email

#FILENAME = "sampleEmails.tar.gz"


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
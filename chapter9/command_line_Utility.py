import argparse # parses the arguments to cmd args
import requests # like fetch - get/post requests

# e.g download a file
def download_file(url,filename):
    if filename is None:
        filename="hello.jpg";
    # Note: stream is True
    with requests.get(url, stream=True) as r:
        r.raise_for_status();
        with open (filename,'wb') as f:
            # if network chunks encoded response uncomment if
            # & set chunks parameter-size to None
            # if chunks:
            for chunks in r.iter_content(chunk_size=None):
                f.write(chunks);
    return filename;

parser = argparse.ArgumentParser();

# argsuments add
parser.add_argument("url",type=str,help = "Url of file to download");

# optional argument
parser.add_argument("-o","--output",help = "Url of file to download",default=None);

# args with type
# parser.add_argument("-n" type=int ,help = "Url of file to download");

args = parser.parse_args();
print(args.url);
print(args.output);
download_file(args.url,args.output);
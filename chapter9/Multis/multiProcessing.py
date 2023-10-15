# Threads are inside a process & are light weight
# Multiprocessing
import requests
import multiprocessing
import concurrent.futures

# function to download files online
def download_file(url,filename):
    print(f"Download Started- {filename}");
    if filename==None:
        print("Error");
        return;
    with requests.get(url,stream=True) as r:
        r.raise_for_status();
        with open(f"imgs\{filename}.jpg",'wb') as f:
            for chunks in r.iter_content(None):
                f.write(chunks);
    print(f"Finished Download- {filename}");
    return filename;

# download_file("https://picsum.photos/900/700",f"img_{0}");
# will take time
# for i in range(1,6):
#     url = 'https://picsum.photos/900/700';
#     download_file("https://picsum.photos/900/700",f"img_{0}");

if __name__ == "__main__":            # now run on shell
    pros = [];
    url = 'https://picsum.photos/900/700';
    for i in range(50):
        p=multiprocessing.Process(target=download_file,args=[url,f"img_{i}"]);
        p.start();
        pros.append(p);

    for p in pros:
        p.join();

# OR simple way using concurrent.futures
if __name__ == "__main__":            # now run on shell
    url = 'https://picsum.photos/900/700';
    with concurrent.futures.ProcessPoolExecutor() as executor:
        lst = [i for i in range(50)]; # list upto 49
        url = [url for i in range(50)];

        # for multiple args give list of every args seperately
        result = executor.map(download_file,url,lst);
        for r in result:
            print(r);


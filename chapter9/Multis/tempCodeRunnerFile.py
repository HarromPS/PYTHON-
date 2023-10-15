tps://picsum.photos/900/700';
for i in range(50):
    p=multiprocessing.Process(target=download_file,args=[url,f"img_{i}"]);
    p.start();
    pros.append(p);

for p in pros:
    p
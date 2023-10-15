# Weather app
import requests
import json

if __name__ == "__main__":

    data = {
            "Transfer-Encoding": "chunked",
            "Connection": "keep-alive",
            "Vary": "Accept-Encoding",
            "CDN-PullZone": "93447",
            "CDN-Uid": "8fa3a04a-75d9-4707-8056-b7b33c8ac7fe",
            "CDN-RequestCountryCode": "GB",
            "CDN-ProxyVer": "1.04",
            "CDN-RequestPullSuccess": "True",
            "CDN-RequestPullCode": "200",
            "CDN-CachedAt": "08/09/2023 12:26:48",
            "CDN-EdgeStorageId": "1076",
            "CDN-Status": "200",
            "CDN-RequestId": "106a9ddc584a917989964a8e8ef2f3b1",
            "CDN-Cache": "MISS",
            "Cache-Control": "public, max-age=180",
            "Content-Type": "application/json",
            "Date": "Wed, 09 Aug 2023 12:26:48 GMT",
            "Server": "BunnyCDN-DE1-1053"
    };

    headers = {
        'Content-type':"application/json;charset=UTF-8"
    }
    country = input("Pass Zipcode, Postcode, Postalcode, IP address, Latitude/Longitude (decimal degree) or city name: ");

    req = requests.post(f"https://api.weatherapi.com/v1/current.json?key=fa3da7a43ee1412792d122428230908&q={country}&aqi=yes",headers=headers,json=data);

    # parse json data as a dictionary
    news = json.loads(req.text);
    # print(type(news));

    # req = requests.post("https://api.weatherapi.com/v1/current.json?key=fa3da7a43ee1412792d122428230908&q=India&aqi=yes",headers);
    with open("A:\VS Codes\Programming\PYTHON\PROJECTS_PY\Weather App\weather.txt",'a') as f:
        f.write(f"\n\nLocation: {news['location']['country']}\n");
        f.write(f"Region: {news['location']['region']}\nName: {news['location']['name']}\n\nTemperature: {news['current']['temp_c']} degree Celcius\nTemperature: {news['current']['temp_f']} degree Fahrenheit\nIcon: https:{news['current']['condition']['icon']}");
        with requests.get(f"https:{news['current']['condition']['icon']}",stream=True) as r:
            r.raise_for_status();
            with open ("A:\VS Codes\Programming\PYTHON\PROJECTS_PY\Weather App\image.png",'wb') as img:
                for contents in r.iter_content(None):
                    img.write(contents);
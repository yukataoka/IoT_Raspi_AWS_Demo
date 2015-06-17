#include <sstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "SeeedOLED.h"

using namespace std;

SeeedOLED oled = SeeedOLED(0x3c);

string GetStdoutFromCommand(string cmd) {
    int len;
    string data;
    FILE * stream;
    const int max_buffer = 256;
    char buffer[max_buffer];
    cmd.append(" 2>&1");

    stream = popen(cmd.c_str(), "r");
    if (stream) {
        while (!feof(stream)) {
            if (fgets(buffer, max_buffer, stream) != NULL) {
                data.append(buffer);
            }
        }
        pclose(stream);
    }
    len = data.size() - 1;
    data = data.substr(0, len);
    return data;
}

int main (int argc, char *argv[])
{
    
    string line0 = "                    ";
    
    string argv1 = line0;
    string argv2 = line0;
    string argv3 = line0;
    string argv4 = line0;
    
    if(argc > 1) argv1 = argv[1];
    if(argc > 2) argv2 = argv[2];
    if(argc > 3) argv3 = argv[3];
    if(argc > 4) argv4 = argv[4];
    
    oled.writeString(0, 0, (char*)line0.c_str());
    oled.writeString(1, 0, (char*)line0.c_str());
    oled.writeString(2, 0, (char*)line0.c_str());
    oled.writeString(3, 0, (char*)line0.c_str());
    
    oled.writeString(0, 0, (char*)argv1.c_str());
    oled.writeString(1, 0, (char*)argv2.c_str());
    oled.writeString(2, 0, (char*)argv3.c_str());
    oled.writeString(3, 0, (char*)argv4.c_str());

    return 0;
}

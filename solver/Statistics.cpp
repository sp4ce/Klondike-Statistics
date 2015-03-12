#include <fstream>

#include "Statistics.h"

using namespace std;

Statistics::Statistics(const char* path) {
    _path = path;
    _data = new map<const char*, int>();
}

void Statistics::Set(const char* name, int data) {
    (*_data)[name] = data;
}

void Statistics::Write() {
    // Test if the file exists.
    bool exists = true;
    ifstream f(_path);
    if (!f.good()) {
        exists = false;
    }

    // The output stream.
    ofstream output(_path, ios::out | ios::app);

    // Output the header.
    if (!exists) {
        writeData(output, true);
    }

    // Output the values
    writeData(output, false);
}

void Statistics::writeData(ofstream& output, bool header) {
    for (map<const char*, int>::iterator it = _data->begin(); it != _data->end(); ++it) {
        if (it != _data->begin()) {
            output << ',';
        }

        if (header) {
            output << it->first;
        } else {
            output << it->second;
        }
    }
    output << endl;
}

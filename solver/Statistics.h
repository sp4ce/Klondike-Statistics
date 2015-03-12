#ifndef Statistics_h
#define Statistics_h

#include <map>

using namespace std;

class Statistics {

private:
    const char* _path;
    map<const char*, int>* _data;

    void writeData(ofstream& output, bool header);

public:
    Statistics(const char* path);
    void Set(const char* name, int data);
    void Write();
};

#endif

#include <iostream>
#include "maxminddb.h"

int main()
{
    std::cout << "MaxMind version: " << MMDB_lib_version() << std::endl;

    return 0;
}

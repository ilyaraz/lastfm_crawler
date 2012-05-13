#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <set>
#include <string>
#include <vector>

int main(int argc, char **argv) {
    std::ifstream input(argv[1]);
    int count = 0;
    std::string temp;
    std::vector<std::string> nodeName;
    std::vector<std::vector<std::string> > neighbors;
    while (getline(input, temp)) {
        ++count;
        std::vector<std::string> tokens;
        std::stringstream ss(temp);
        std::string token;
        while (ss >> token) {
            tokens.push_back(token);
        }
        nodeName.push_back(tokens[0]);
        tokens.erase(tokens.begin());
        neighbors.push_back(tokens);
    }

    std::map<std::string, int> nodes;
    for (size_t i = 0; i < nodeName.size(); ++i) {
        nodes[nodeName[i]] = i;
    }
    std::vector<std::vector<int> > graph(nodeName.size());
    for (size_t i = 0; i < nodeName.size(); ++i) {
        for (std::vector<std::string>::const_iterator it = neighbors[i].begin(); it != neighbors[i].end(); ++it) {
            if (nodes.count(*it)) {
                graph[i].push_back(nodes[*it]);
            }
        }
    }
    std::cout<< graph.size() << std::endl;
    for (size_t i = 0; i < graph.size(); ++i) {
        for (size_t j = 0; j < graph[i].size(); ++j) {
            if (i < graph[i][j]) {
                std::cout << i << " " << graph[i][j] << std::endl;
            }
        }
    }
    return 0;
}

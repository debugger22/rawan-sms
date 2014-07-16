#define BOOST_PYTHON_STATIC_LIB
#include <boost/python.hpp>

using namespace boost::python;
using namespace std;

class CompareObject {
    public:
    bool  operator()(const LinkScore& l, const LinkScore& r) { return l.score_ > r.score_; }
};

list get_scores(object links)
{
    object utility = import("links.utility");
    set<LinkScore, CompareObject> seen_links;
    list python_seen_links;
    for (int i = 0; i < len(links); ++i)
    {
        const object& link = links[i];
        LinkScore score = LinkScore(link, score_link (link, links));
        auto iter = seen_links.find(score);

        if (iter != seen_links.end())
        {
            // Do stuff
        }
        else
        {
            // Do other stuff
        }
    }
    // TODO: Optimize this
    for (auto i = seen_links.begin(); i != seen_links.end(); ++i)
    {
        python_seen_links.append(*i);
    }
    return python_seen_links;
}

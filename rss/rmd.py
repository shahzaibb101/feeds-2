import re
from html import unescape

summary = """<p>Reuters was ahead to report that Sonkichi Sakihara recalls chancing upon some of the last refugees to arrive on Yonaguni: [&#8230;]</p>
<p>The post <a href="https://www.reutersagency.com/en/reutersbest/article/japans-frontier-islanders-decry-lack-of-plan-to-aid-taiwanese-fleeing-attack/">Japan&#8217;s frontier islanders decry lack of plan to aid Taiwanese fleeing attack </a> appeared first on <a href="https://www.reutersagency.com/en/">Reuters News Agency</a>.</p>"""

# Use regular expression to remove HTML tags
clean_summary = re.sub('<.*?>', '', summary)
clean_summary = unescape(clean_summary)

print(clean_summary)

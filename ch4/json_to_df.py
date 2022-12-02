# pp 68

data = [{"Emp":"Jeff Russell",
"POs":[{"Pono":2608,"Total":35},
{"Pono":2617,"Total":35},
{"Pono":2620,"Total":139}
]},
{"Emp":"Jane Boorman",
"POs":[{"Pono":2621,"Total":95},
{"Pono":2626,"Total":218}
]
}]

import json
import pandas as pd
df = pd.json_normalize(data, "POs", "Emp").set_index(["Emp","Pono"])
print(df)

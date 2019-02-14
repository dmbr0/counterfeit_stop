#!/usr/bin/env python
import strgen 

print(strgen.StringGenerator("[\d\w]{10}").render_list(20,unique=True))

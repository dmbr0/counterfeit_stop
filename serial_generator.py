#!/usr/bin/env python
import strgen 


print(strgen.StringGenerator("[\d\w]{7}").render_list(20,unique=True))

// mapping record from [in_min, out_min] to [out_min, out_max]
// using liner change
// x --> in_final_record, y--> in_full_time_record
// the result keep in_full_time_record not changed

def map_range(x, y, in_min, in_max, out_min, out_max):
   m = (out_max - out_min) / (in_max - in_min)
   return (out_min + m * (x - in_min) - y*0.3) / 0.7

// sample   
f = lambda x, y: map_range(x, y, 69, 96.5, 80, 100)

f(89.2, 92)

#!/usr/bin/env ruby
# Match hbn,hbtn and the t character in between if repeated for n times
puts ARGV[0].scan(/hbt*n/).join

#!/usr/bin/env ruby
# The REGEX that will match "hbttn - hbtttttn" and nothing else i.e repetitive 't' 
puts ARGV[0].scan(/hbt{2,5}n/).join

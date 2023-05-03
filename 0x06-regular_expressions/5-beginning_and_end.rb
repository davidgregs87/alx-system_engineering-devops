#!/usr/bin/env ruby
# Match h in the beginning, n at the end and any single character in the middle
puts ARGV[0].scan(/^h\wn$/).join

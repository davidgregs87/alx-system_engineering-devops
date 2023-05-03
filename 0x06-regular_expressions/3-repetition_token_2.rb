#!/usr/bin/env ruby
# Match the character t to it's 4th repetition
puts ARGV[0].scan(/hbt{1,4}n/).join

#!/usr/bin/env ruby
# Match "htn and hbtn" only
puts ARGV[0].scan(/hb{0,1}tn/).join

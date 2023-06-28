# Install and configure nginx with puppet

package { 'nginx':
  ensure  =>  installed,
}

file { '/var/www/html/index.html':
  content  =>  'Hello World!',
}

service { 'nginx':
  ensure  =>  running,
  require =>  Package['nginx']
}

file_line { 'server_config':
  ensure  =>  present,
  path    =>  '/etc/nginx/sites-available/default',
  after   =>  'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://stackoverflow.com/ permanent;'
}

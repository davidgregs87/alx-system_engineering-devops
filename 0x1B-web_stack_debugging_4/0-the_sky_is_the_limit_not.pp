file { '/etc/default/nginx':
  ensure => file,
  before => Exec['restart-nginx'],
  content => template('my_module/nginx_default.erb'), # Use a template with the necessary configuration
}

exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}

# You can place the file content in a template located in your module's templates directory
# my_module/templates/nginx_default.erb
# ulimit -n=<%= scope.function_ulimit(['nofile']) %>

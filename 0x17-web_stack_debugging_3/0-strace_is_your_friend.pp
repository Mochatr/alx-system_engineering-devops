# This manifest fixes the Apache 500 error by setting file permissions

exec {
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

# This manifest optimizes Nginx for high traffic. 

exec { 'set ulimit -n 2048':
  command => "sed -i 's/15/2048/' /etc/default/nginx",
  path    => ['/bin/', '/sbin/', '/usr/bin/'n '/usr/sbin/'],
  }

exec { 'restart service':
  command => 'service nginx restart',
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
  }

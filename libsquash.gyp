# Copyright (c) 2017 Minqi Pan <pmq2001@gmail.com>
#                    Shengyuan Liu <sounder.liu@gmail.com>
# 
# This file is part of libsquash, distributed under the MIT License
# For full terms see the included LICENSE file

{
  'targets': [
    {
      'target_name': 'libsquash',
      'type': 'static_library',
      'sources': [
        'include/squash.h',
        'include/squash/cache.h',
        'include/squash/common.h',
        'include/squash/decompress.h',
        'include/squash/dir.h',
        'include/squash/dirent.h',
        'include/squash/fdtable.h',
        'include/squash/file.h',
        'include/squash/fs.h',
        'include/squash/hash.h',
        'include/squash/nonstd.h',
        'include/squash/private.h',
        'include/squash/squashfs_fs.h',
        'include/squash/stack.h',
        'include/squash/table.h',
        'include/squash/traverse.h',
        'include/squash/util.h',
        'include/squash/windows.h',
        'src/cache.c',
        'src/decompress.c',
        'src/dir.c',
        'src/dirent.c',
        'src/fd.c',
        'src/file.c',
        'src/fs.c',
        'src/hash.c',
        'src/nonstd-makedev.c',
        'src/nonstd-stat.c',
        'src/private.c',
        'src/readlink.c',
        'src/scandir.c',
        'src/squash.c',
        'src/stack.c',
        'src/stat.c',
        'src/table.c',
        'src/traverse.c',
        'src/util.c',
      ],
      'include_dirs': [
        'include',
      ],
    },
  ],
}

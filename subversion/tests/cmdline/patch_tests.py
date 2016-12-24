  patch_file_path = sbox.get_tempname('my.patch')
  expected_output = wc.State(wc_dir, {
    'A/D/gamma'  : Item(status='U '),
    'iota'       : Item(status='U '),
    'new'        : Item(status='A '),
    'A/mu'       : Item(status='U '),
    'A/B/E/beta' : Item(status='D '),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       [], True, True)
  # Retry
  expected_output.tweak(status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True)
  patch_file_path = os.path.abspath(sbox.get_tempname('my.patch'))
  svntest.actions.run_and_verify_patch('', patch_file_path,
  patch_file_path = os.path.abspath(sbox.get_tempname('my.patch'))
  svntest.actions.run_and_verify_patch('', patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
                                       patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  expected_status.tweak('A/D/H/chi', status='! ')
  expected_status.tweak('A/D/H/omega', 'A/D/H/psi', 'A/B', 'A/B/E',
                        'A/B/E/beta', 'A/B/E/alpha', 'A/B/lambda',
                        'A/B/F', status='D ')
                                       patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  # Strict EOL style matching breaks Windows tests at least with Python 2
  keep_eol_style = not svntest.main.is_os_windows()

      expected_output = wc.State(wc_dir, {
        'A/mu' : Item(status='U '),
      })
      svntest.actions.run_and_verify_patch2(wc_dir,
                                            patch_file_path,
                                            expected_output,
                                            expected_disk,
                                            expected_status,
                                            expected_skip,
                                            [], True, True, keep_eol_style)
      svntest.actions.run_and_verify_svn(expected_output, [],
                                         'revert', '-R', wc_dir)
  patch_file_path = sbox.get_tempname('my.patch')
  # Strict EOL style matching breaks Windows tests at least with Python 2
  keep_eol_style = not svntest.main.is_os_windows()

      svntest.actions.run_and_verify_patch2(wc_dir,
                                            patch_file_path,
                                            expected_output,
                                            expected_disk,
                                            expected_status,
                                            expected_skip,
                                            None, # expected err
                                            1, # check-props
                                            1, # dry-run
                                            keep_eol_style) # keep-eol-style
  patch_file_path = sbox.get_tempname('my.patch')
  # Strict EOL style matching breaks Windows tests at least with Python 2
  keep_eol_style = not svntest.main.is_os_windows()

      expected_output = wc.State(wc_dir, {
        'A/mu' : Item(status='U '),
      })
      svntest.actions.run_and_verify_patch2(wc_dir,
                                            patch_file_path,
                                            expected_output,
                                            expected_disk,
                                            expected_status,
                                            expected_skip,
                                            None, # expected err
                                            1, # check-props
                                            1, # dry-run
                                            keep_eol_style) # keep-eol-style
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, ''.join(unidiff_patch), 'wb')
  expected_skip = wc.State(wc_dir, { })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       [], True, True)
  # And repeat
  expected_output = svntest.wc.State(wc_dir, {
    'iota' : Item(status=' G')
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True)

  # Reverse
  expected_output.tweak('iota', status=' U')
  expected_status.tweak('iota', status='  ')
  expected_disk.tweak('iota',
                      props={'deleted': "This is the property 'deleted'.\n",
                             'modified': "This is the property 'modified'.\n"})
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Repeat
  expected_output.tweak('iota', status=' G')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And now try against a not existing target
  svntest.actions.run_and_verify_svn(None, [],
                                     'rm', '--force', sbox.ospath('iota'))
  expected_output.remove('iota')
  expected_disk.remove('iota')
  expected_status.tweak('iota', status='D ')
  expected_skip.add({
    'iota' : Item(verb='Skipped'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True)

  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
    # with no trailing context. Originally, Subversion applied this patch
    # multiple times, which matched the behaviour of Larry Wall's patch
    # implementation.
    '>         hunk @@ -1,1 +1,2 @@ already applied\n',
    'G         %s\n' % sbox.ospath('A/B/E/beta'),
    '>         hunk @@ -1,1 +0,0 @@ already applied\n',
  ]
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
    '>         rejected hunk ## -0,0 +1,1 ## (svn:executable)\n',
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = os.path.abspath(sbox.get_tempname('my.patch'))
  svntest.actions.run_and_verify_patch('', patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
    "new file mode 100644\n",
    "deleted file mode 100644\n",
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  expected_output = wc.State(wc_dir, {
    'A/D/gamma'   : Item(status='U '),
    'iota'        : Item(status='U '),
    'new'         : Item(status='A '),
    'A/mu'        : Item(status='U '),
    'A/B/E/beta'  : Item(status='D '),
  })
  expected_skip = wc.State(wc_dir, { })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       [], True, True)

  # Try again
  expected_output.tweak(status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True)
  expected_output = wc.State(wc_dir, {
    'A/D/gamma'   : Item(status='U '),
    'iota'        : Item(status='U '),
    'new'         : Item(status='D '),
    'A/mu'        : Item(status='U '),
    'A/B/E/beta'  : Item(status='A '),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       [], True, True,
                                       '--reverse-diff')

  # And again
  expected_output.tweak(status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True,
  patch_file_path = sbox.get_tempname('my.patch')
    unidiff_patch += ['\ No newline at end of property\n']
  svntest.main.file_write(patch_file_path, ''.join(unidiff_patch), 'wb')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  svntest.actions.check_prop('k', wc_dir, [value.encode()])
  patch_file_path = sbox.get_tempname('my.patch')
    "\\ No newline at end of file\n"
    "\\ No newline at end of property\n"
  expected_output = svntest.wc.State(wc_dir, {
    'iota_symlink' : Item(status='A ')
  })
  if not svntest.main.is_posix_os():
    expected_disk.tweak('iota_symlink', contents='link iota')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       [], True, True)

  # And again
  expected_output.tweak('iota_symlink', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True)

  # Reverse
  expected_output.tweak('iota_symlink', status='D ')
  expected_disk.remove('iota_symlink')
  expected_status.remove('iota_symlink')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And again
  expected_output.tweak('iota_symlink', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       [], True, True,
                                       '--reverse-diff')
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  expected_disk.tweak('iota', contents=iota_contents + "Some more bytes\n")
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       1) # dry-run
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = os.path.abspath(sbox.get_tempname('my.patch'))
  svntest.actions.run_and_verify_patch('', patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  wc_dir = sbox.wc_dir
  patch_file_path = sbox.get_tempname('my.patch')
  expected_output = wc.State(wc_dir, {
    'A/D/G/pi'     : Item(status='D '),
    'A/D/G/rho'    : Item(status='D '),
    'A/D/G/tau'    : Item(status='D '),
    'A/D/G'        : Item(status='D '),
    'A/D/H/chi'    : Item(status='D '),
    'A/D/H/omega'  : Item(status='D '),
    'A/D/H/psi'    : Item(status='D '),
    'A/D/H'        : Item(status='D '),
    'A/D/gamma'    : Item(status='D '),
    'A/D'          : Item(status='A ', prev_status='D '),
    'iota'         : Item(status='A ', prev_status='D '),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.remove('A/D/G/rho', 'A/D/G/pi', 'A/D/G/tau',
                         'A/D/H/psi', 'A/D/H/omega', 'A/D/H/chi',
                         'A/D/gamma', 'A/D/G', 'A/D/H')
  expected_status.tweak('A/D', status='R ')
  expected_status.tweak('iota', status='RM')
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.remove('A/D/G/rho', 'A/D/G/pi', 'A/D/G/tau',
                       'A/D/H/psi', 'A/D/H/omega', 'A/D/H/chi',
                       'A/D/gamma', 'A/D', 'A/D/G', 'A/D/H')
  expected_disk.add({
    'A/D' : Item(contents="New file"),
    'iota' : Item(contents="", props={u'k': u'v'}),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)
  patch_file_path = sbox.get_tempname('my.patch')
  expected_output = wc.State(wc_dir, {
    'test' : Item(status='C ')
  })
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'test' : Item(status='  ', wc_rev='2'),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'test'              : Item(contents="line"),
    'test.svnpatch.rej' : Item(contents="--- test\n"
                                        "+++ test\n"
                                        "@@ -1,1 +1,1 @@\n"
                                        "-foo\n"
                                        "\\ No newline at end of file\n"
                                        "+bar\n"
                                        "\\ No newline at end of file\n"),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)
  patch_file_path = sbox.get_tempname('my.patch')
    "-\n"
    'lf.txt'            : Item(contents="replacement\n"),
  expected_skip = wc.State(wc_dir, {})
  expected_status = None
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)
  test1_body = '\n'.join([
    ])
  svntest.main.file_write(sbox.ospath('test.txt'), test1_body, 'wb')
  test2_body = '\n'.join([
    ])
  svntest.main.file_write(sbox.ospath('test_v2.txt'), test2_body, 'wb')
  patch_path = sbox.get_tempname('patch.diff')
  svntest.main.file_write(patch_path, ''.join(out_text), 'wb')
  expected_output = wc.State(wc_dir, {
    'test.txt' : Item(status='U '),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'test.txt' : Item(contents=test2_body),
    'test_v2.txt' : Item(contents=test2_body),
  })
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'test_v2.txt'       : Item(status='A ', wc_rev='-'),
    'test.txt'          : Item(status='A ', wc_rev='-'),
  })
  expected_skip = wc.State(wc_dir, {})

  svntest.actions.run_and_verify_patch(wc_dir, patch_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  expected_output = wc.State(wc_dir, {
    'iota' : Item(status='U ')
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  expected_output = wc.State(wc_dir, {
    'iota'  : Item(status='D '),
    'iota2' : Item(status='A ')
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output = wc.State(wc_dir, {
    'iota2' : Item(status='G ')
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Reverse
  expected_output = wc.State(wc_dir, {
    'iota2' : Item(status='D '),
    'iota'  : Item(status='A '),
  })
  expected_disk.remove('iota2')
  expected_disk.add({
    'iota'              : Item(contents="This is the file 'iota'.\n"),
  })
  expected_status.remove('iota2')
  expected_status.tweak('iota', moved_to=None, status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Retry reverse
  # svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  #                                      expected_output, expected_disk,
  #                                      expected_status, expected_skip,
  #                                      [], True, True,
  #                                      '--reverse-diff')
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  # Second application notifies already applied
    'G         %s\n' % sbox.ospath('A/B/E/beta'),
    '>         hunk @@ -1,1 +0,0 @@ already applied\n',
  ]
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
    "+++ /dev/null\n",
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  os.remove(sbox.ospath('A/mu.svnpatch.rej'))
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  os.remove(sbox.ospath('A/mu.svnpatch.rej'))
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  os.remove(sbox.ospath('A/mu.svnpatch.rej'))
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
  os.remove(sbox.ospath('A/mu.svnpatch.rej'))
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)

@SkipUnless(svntest.main.is_posix_os)
def patch_symlink_traversal(sbox):
  """symlink traversal behaviour"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir
  alpha_contents = "This is the file 'alpha'.\n"

  # A/B/E/unversioned -> alpha
  # A/B/E/versioned -> alpha
  # A/B/unversioned -> E         (so A/B/unversioned/alpha is A/B/E/alpha)
  # A/B/versioned -> E           (so A/B/versioned/alpha is A/B/E/alpha)
  os.symlink('alpha', sbox.ospath('A/B/E/unversioned'))
  os.symlink('alpha', sbox.ospath('A/B/E/versioned'))
  os.symlink('E', sbox.ospath('A/B/unversioned'))
  os.symlink('E', sbox.ospath('A/B/versioned'))
  sbox.simple_add('A/B/E/versioned', 'A/B/versioned')

  prepatch_status = svntest.actions.get_virginal_state(wc_dir, 1)
  prepatch_status.add({'A/B/E/versioned' : Item(status='A ', wc_rev='-')})
  prepatch_status.add({'A/B/versioned' : Item(status='A ', wc_rev='-')})
  svntest.actions.run_and_verify_status(wc_dir, prepatch_status)

  # Patch through unversioned symlink to file
  unidiff_patch = (
    "Index: A/B/E/unversioned\n"
    "===================================================================\n"
    "--- A/B/E/unversioned\t(revision 2)\n"
    "+++ A/B/E/unversioned\t(working copy)\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = wc.State(wc_dir, {
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({'A/B/E/unversioned' : Item(contents=alpha_contents)})
  expected_disk.add({'A/B/E/versioned' : Item(contents=alpha_contents)})
  expected_disk.add({'A/B/unversioned' : Item()})
  expected_disk.add({'A/B/versioned' : Item()})
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({'A/B/E/versioned' : Item(status='A ', wc_rev='-')})
  expected_status.add({'A/B/versioned' : Item(status='A ', wc_rev='-')})
  expected_skip = wc.State(wc_dir, {
    'A/B/E/unversioned' : Item(verb='Skipped'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)
  svntest.actions.run_and_verify_status(wc_dir, prepatch_status)

  # Patch through versioned symlink to file
  unidiff_patch = (
    "Index: A/B/E/versioned\n"
    "===================================================================\n"
    "--- A/B/E/versioned\t(revision 2)\n"
    "+++ A/B/E/versioned\t(working copy)\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)
  reject_contents = (
    "--- A/B/E/versioned\n"
    "+++ A/B/E/versioned\n"
    "@@ -1,1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
  )

  expected_output = wc.State(wc_dir, {
    'A/B/E/versioned' : Item(status='C ')
  })
  expected_disk.add({
     'A/B/E/versioned.svnpatch.rej' : Item(contents=reject_contents)
  })
  expected_skip = wc.State(wc_dir, { })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)
  os.remove(sbox.ospath('A/B/E/versioned.svnpatch.rej'))
  expected_disk.remove('A/B/E/versioned.svnpatch.rej')
  svntest.actions.run_and_verify_status(wc_dir, prepatch_status)

  # Patch through unversioned symlink to parent of file
  unidiff_patch = (
    "Index: A/B/unversioned/alpha\n"
    "===================================================================\n"
    "--- A/B/unversioned/alpha\t(revision 2)\n"
    "+++ A/B/unversioned/alpha\t(working copy)\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = wc.State(wc_dir, {})
  expected_skip = wc.State(wc_dir, {
    'A/B/unversioned/alpha' : Item(verb='Skipped'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)
  svntest.actions.run_and_verify_status(wc_dir, prepatch_status)

  # Patch through versioned symlink to parent of file
  unidiff_patch = (
    "Index: A/B/versioned/alpha\n"
    "===================================================================\n"
    "--- A/B/versioned/alpha\t(revision 2)\n"
    "+++ A/B/versioned/alpha\t(working copy)\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = wc.State(wc_dir, {})
  expected_skip = wc.State(wc_dir, {
    'A/B/versioned/alpha' :  Item(verb='Skipped'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)
  svntest.actions.run_and_verify_status(wc_dir, prepatch_status)

@SkipUnless(svntest.main.is_posix_os)
def patch_obstructing_symlink_traversal(sbox):
  """obstructing symlink traversal behaviour"""

  sbox.build()
  wc_dir = sbox.wc_dir
  alpha_contents = "This is the file 'alpha'.\n"
  sbox.simple_append('A/B/F/alpha', alpha_contents)
  sbox.simple_add('A/B/F/alpha')
  sbox.simple_commit()
  sbox.simple_update()

  # Unversioned symlink A/B/E -> F obstructing versioned A/B/E so
  # versioned A/B/E/alpha is A/B/F/alpha
  svntest.main.safe_rmtree(sbox.ospath('A/B/E'))
  os.symlink('F', sbox.ospath('A/B/E'))

  unidiff_patch = (
    "Index: A/B/E/alpha\n"
    "===================================================================\n"
    "--- A/B/E/alpha\t(revision 2)\n"
    "+++ A/B/E/alpha\t(working copy)\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'alpha'.\n"
    "+xx\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  ### Patch applies through the unversioned symlink
  expected_output = [
    'U         %s\n' % sbox.ospath('A/B/E/alpha'),
  ]
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.remove('A/B/E/alpha', 'A/B/E/beta')
  expected_disk.add({'A/B/F/alpha' : Item(contents=alpha_contents+"xx\n")})
  expected_status = svntest.actions.get_virginal_state(wc_dir, 2)
  expected_status.add({'A/B/F/alpha' : Item(status='  ', wc_rev=2)})
  expected_status.tweak('A/B/E', status='~ ')
  expected_status.tweak('A/B/E/alpha', 'A/B/F/alpha', status='M ')
  expected_status.tweak('A/B/E/beta', status='! ')
  expected_skip = wc.State('', { })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
def patch_binary_file(sbox):
  "patch a binary file"

  sbox.build()
  wc_dir = sbox.wc_dir

  # Make the file binary by putting some non ascii chars inside or propset
  # will return a warning
  sbox.simple_append('iota', b'\0\202\203\204\205\206\207nsomething\nelse\xFF')
  sbox.simple_propset('svn:mime-type', 'application/binary', 'iota')

  expected_output = [
    'Index: svn-test-work/working_copies/patch_tests-57/iota\n',
    '===================================================================\n',
    'diff --git a/iota b/iota\n',
    'GIT binary patch\n',
    'literal 48\n',
    'zc$^E#$ShU>qLPeMg|y6^R0Z|S{E|d<JuZf(=9bpB_PpZ!+|-hc%)E52)STkf{{Wp*\n',
    'B5)uFa\n',
    '\n',
    'literal 25\n',
    'ec$^E#$ShU>qLPeMg|y6^R0Z|S{E|d<JuU!m{s;*G\n',
    '\n',
    'Property changes on: iota\n',
    '___________________________________________________________________\n',
    'Added: svn:mime-type\n',
    '## -0,0 +1 ##\n',
    '+application/binary\n',
    '\ No newline at end of property\n',
  ]

  _, diff_output, _ = svntest.actions.run_and_verify_svn(expected_output, [],
                                                         'diff', '--git',
                                                         wc_dir)

  sbox.simple_revert('iota')

  tmp = sbox.get_tempname()
  svntest.main.file_write(tmp, ''.join(diff_output))

  expected_output = wc.State(wc_dir, {
    'iota'              : Item(status='UU'),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota',
                      props={'svn:mime-type':'application/binary'},
                      contents =
                      b'This is the file \'iota\'.\n' +
                      b'\0\202\203\204\205\206\207nsomething\nelse\xFF')
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', status='MM')
  expected_skip = wc.State('', { })

  svntest.actions.run_and_verify_patch(wc_dir, tmp,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Ok, now try applying it backwards
  expected_output.tweak('iota', status='UU')
  expected_disk = svntest.main.greek_state.copy()
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  svntest.actions.run_and_verify_patch(wc_dir, tmp,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

def patch_delete_nodes(sbox):
  "apply deletes via patch"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_propset('A', 'B', 'A/B/E/alpha')
  sbox.simple_append('A/mu', '\0')
  sbox.simple_propset('svn:mime-type', 'application/nonsense', 'A/mu')

  sbox.simple_commit() # r2
  sbox.simple_update()

  expected_skip = wc.State('', { })

  original_status = svntest.actions.get_virginal_state(wc_dir, 2)
  original_disk = svntest.main.greek_state.copy()
  original_disk.tweak('A/mu',
                      props={'svn:mime-type':'application/nonsense'},
                      contents = 'This is the file \'mu\'.\n\0')
  original_disk.tweak('A/B/E/alpha', props={'A':'B'})
  svntest.actions.run_and_verify_status(wc_dir, original_status)
  svntest.actions.verify_disk(wc_dir, original_disk, True)

  sbox.simple_rm('A/B/E/alpha', 'A/B/E/beta', 'A/mu')

  _, diff, _ = svntest.actions.run_and_verify_svn(None, [],
                                                  'diff', '--git', wc_dir)

  patch = sbox.get_tempname('patch')
  svntest.main.file_write(patch, ''.join(diff))

  deleted_status = original_status.copy()
  deleted_disk = original_disk.copy()
  deleted_disk.remove('A/B/E/alpha', 'A/B/E/beta', 'A/mu')
  deleted_status.tweak('A/B/E/alpha', 'A/B/E/beta', 'A/mu', status='D ')


  svntest.actions.run_and_verify_status(wc_dir, deleted_status)
  svntest.actions.verify_disk(wc_dir, deleted_disk, True)

  # And now apply the patch from the clean state
  sbox.simple_revert('A/B/E/alpha', 'A/B/E/beta', 'A/mu')

  # Expect that the hint 'empty dir? -> delete dir' deletes 'E'
  # ### A smarter diff format might change this in a future version
  deleted_disk.remove('A/B/E')
  deleted_status.tweak('A/B/E', status='D ')
  expected_output = wc.State(wc_dir, {
    'A/mu'              : Item(status='D '),
    'A/B/E'             : Item(status='D '),
    'A/B/E/beta'        : Item(status='D '),
    'A/B/E/alpha'       : Item(status='D '),
  })

  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, deleted_disk,
                                       deleted_status, expected_skip,
                                       [], False, True)

  # And let's see if we can apply the reverse version of the patch
  expected_output = wc.State(wc_dir, {
    'A/mu'              : Item(status='A '),
    'A/B/E'             : Item(status='A '),
    'A/B/E/beta'        : Item(status='A '),
    'A/B/E/alpha'       : Item(status='A '),
  })
  original_status.tweak('A/mu', status='RM') # New file
  original_status.tweak('A/B/E', status='R ') # New dir
  original_status.tweak('A/B/E/alpha', 'A/B/E/beta',
                        status='A ', wc_rev='-',
                        entry_status='R ', entry_rev='2')


  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, original_disk,
                                       original_status, expected_skip,
                                       [], True, True, '--reverse-diff')

def patch_delete_missing_eol(sbox):
  "apply a delete missing an eol"

  sbox.build(read_only = True)
  wc_dir = sbox.wc_dir

  delete_patch = [
    "Index: A/B/E/beta\n",
    "===================================================================\n",
    "--- A/B/E/beta	(revision 1)\n",
    "+++ /dev/null\n",
    "@@ -1 +0,0 @@\n",
    "-This is the file 'beta'." # No final EOL
  ]

  patch = sbox.get_tempname('patch')
  svntest.main.file_write(patch, ''.join(delete_patch))

  expected_output = wc.State(wc_dir, {
    'A/B/E/beta'        : Item(status='D '),
  })
  expected_skip = wc.State(wc_dir, {
  })
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('A/B/E/beta', status='D ')
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.remove('A/B/E/beta')

  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # Try again? -> Merged
  expected_output = wc.State(wc_dir, {
    'A/B/E/beta'        : Item(status='G '),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # Reverse
  expected_output = wc.State(wc_dir, {
    'A/B/E/beta'        : Item(status='A '),
  })
  expected_skip = wc.State(wc_dir, {
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_status.tweak('A/B/E/beta', status='R ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

  # Try again? -> Already applied
  expected_output = wc.State(wc_dir, {
    'A/B/E/beta'        : Item(status='G '),
  })
  expected_skip = wc.State(wc_dir, {
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

def patch_final_eol(sbox):
  "patch the final eol"

  sbox.build()
  wc_dir = sbox.wc_dir

  delete_patch = [
   'Index: A/mu\n',
   '===================================================================\n',
   '--- A/mu\t(revision 1)\n',
   '+++ A/mu\t(working copy)\n',
   '@@ -1 +1 @@\n',
   '-This is the file \'mu\'.\n',
   '+This is the file \'mu\'.\n',
   '\ No newline at end of file\n',
   'Index: iota\n',
   '===================================================================\n',
   '--- iota\t(revision 1)\n',
   '+++ iota\t(working copy)\n',
   '@@ -1 +1 @@\n',
   '-This is the file \'iota\'.\n',
   '+This is the file \'iota\'.\n',
   '\ No newline at end of file' # Missing EOL
  ]

  patch = sbox.get_tempname('patch')
  # We explicitly use wb here as this is the eol type added later in the test
  svntest.main.file_write(patch, ''.join(delete_patch), mode='wb')

  expected_output = wc.State(wc_dir, {
    'A/mu'        : Item(status='U '),
    'iota'        : Item(status='U '),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', 'A/mu', status='M ')
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota', contents="This is the file 'iota'.")
  expected_disk.tweak('A/mu', contents="This is the file 'mu'.")

  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # And again - Still U as patch doesn't check final EOL of source
  expected_output.tweak('iota', 'A/mu', status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # Reverse
  expected_output.tweak('iota', 'A/mu', status='U ')
  expected_disk.tweak('iota', contents="This is the file 'iota'.\n")
  expected_disk.tweak('A/mu', contents="This is the file 'mu'.\n")
  expected_status.tweak('iota', 'A/mu', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

  # And once more
  expected_output.tweak('iota', 'A/mu', status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

  # Change the unmodified form
  sbox.simple_append('iota', 'This is the file \'iota\'.', truncate=True)
  sbox.simple_append('A/mu', 'This is the file \'mu\'.', truncate=True)
  sbox.simple_commit()
  expected_status.tweak('iota', 'A/mu', wc_rev='2')

  add_patch = [
    'Index: A/mu\n',
    '===================================================================\n',
    '--- A/mu\t(revision 2)\n',
    '+++ A/mu\t(working copy)\n',
    '@@ -1 +1 @@\n',
    '-This is the file \'mu\'.\n',
    '\ No newline at end of file\n',
    '+This is the file \'mu\'.\n',
    'Index: iota\n',
    '===================================================================\n',
    '--- iota\t(revision 2)\n',
    '+++ iota\t(working copy)\n',
    '@@ -1 +1 @@\n',
    '-This is the file \'iota\'.\n',
    '\ No newline at end of file\n',
    '+This is the file \'iota\'.' # Missing eol
  ]

  svntest.main.file_write(patch, ''.join(add_patch), mode='wb')

  # Apply the patch
  expected_output.tweak('iota', 'A/mu', status='U ')
  expected_disk.tweak('iota', contents="This is the file 'iota'.\n")
  expected_disk.tweak('A/mu', contents="This is the file 'mu'.\n")
  expected_status.tweak('iota', 'A/mu', status='M ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # And again
  expected_output.tweak('iota', 'A/mu', status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True)

  # And in reverse
  expected_output.tweak('iota', 'A/mu', status='U ')
  expected_disk.tweak('iota', contents="This is the file 'iota'.")
  expected_disk.tweak('A/mu', contents="This is the file 'mu'.")
  expected_status.tweak('iota', 'A/mu', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

  # And again
  expected_output.tweak('iota', 'A/mu', status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

def patch_adds_executability_nocontents(sbox):
  """patch adds svn:executable, without contents"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  unidiff_patch = (
    "diff --git a/iota b/iota\n"
    "old mode 100644\n"
    "new mode 100755\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = wc.State(wc_dir, {
    'iota' : Item(status=' U')
  })
  expected_disk = svntest.main.greek_state.copy()
  # "*" is SVN_PROP_EXECUTABLE_VALUE aka SVN_PROP_BOOLEAN_TRUE
  expected_disk.tweak('iota', props={'svn:executable': '*'})

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', status=' M')

  expected_skip = wc.State(wc_dir, { })

  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       check_props=True)

  # And try it again
  # This may produce different output but must have the same result
  expected_output.tweak('iota', status=' G')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       check_props=True)

  # And then try it in reverse
  expected_disk.tweak('iota', props={})
  expected_status.tweak('iota', status='  ')
  expected_output.tweak('iota', status=' U')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True, '--reverse-diff')

  # And try it again
  # This may produce different output but must have the same result
  expected_output.tweak('iota', status=' G')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True, '--reverse-diff')

def patch_adds_executability_nocontents2(sbox):
  "patch adds svn:executable, without contents 2"

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  unidiff_patch = (
    "diff --git a/new b/new\n"
    "old mode 100644\n"
    "new mode 100755\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = wc.State(wc_dir, {
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)

  expected_skip = wc.State(wc_dir, {
    'new' : Item(verb='Skipped missing target')
  })

  # This creates 'new', while a skip or reject is expected
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)


def patch_adds_executability_yescontents(sbox):
  """patch adds svn:executable, with contents"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  mu_new_contents = (
    "This is the file 'mu'.\n"
    "with text mods too\n"
    )

  unidiff_patch = (
    "diff --git a/A/mu b/A/mu\n"
    "old mode 100644\n"
    "new mode 100755\n"
    "index 8a0f01c..dfad3ac\n"
    "--- a/A/mu\n"
    "+++ b/A/mu\n"
    "@@ -1 +1,2 @@\n"
    " This is the file 'mu'.\n"
    "+with text mods too\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = [
    'UU        %s\n' % sbox.ospath('A/mu'),
  ]
  expected_disk = svntest.main.greek_state.copy()
  # "*" is SVN_PROP_EXECUTABLE_VALUE aka SVN_PROP_BOOLEAN_TRUE
  expected_disk.tweak('A/mu', props={'svn:executable': '*'})
  expected_disk.tweak('A/mu', contents=mu_new_contents)

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('A/mu', status='MM')

  expected_skip = wc.State('', { })

  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       check_props=True)

def patch_deletes_executability(sbox):
  """patch deletes svn:executable"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  ## Set up the basic state.
  sbox.simple_propset('svn:executable', 'yes', 'iota')
  #sbox.simple_commit(target='iota', message="Make 'iota' executable.")

  unidiff_patch = (
    "diff --git a/iota b/iota\n"
    "old mode 100755\n"
    "new mode 100644\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = [
    ' U        %s\n' % sbox.ospath('iota'),
  ]
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota') # props=None by default

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', status='  ')

  expected_skip = wc.State('', { })

  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       check_props=True)

def patch_ambiguous_executability_contradiction(sbox):
  """patch ambiguous svn:executable, bad"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  unidiff_patch = (
    "Index: iota\n"
    "===================================================================\n"
    "diff --git a/iota b/iota\n"
    "old mode 100755\n"
    "new mode 100644\n"
    "Property changes on: iota\n"
    "-------------------------------------------------------------------\n"
    "Added: svn:executable\n"
    "## -0,0 +1 ##\n"
    "+*\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = []

  expected_disk = svntest.main.greek_state.copy()

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)

  expected_skip = wc.State('', { })

  error_re_string = r'.*Invalid patch:.*contradicting.*mode.*svn:executable'
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       error_re_string=error_re_string,
                                       check_props=True)

def patch_ambiguous_executability_consistent(sbox):
  """patch ambiguous svn:executable, good"""

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  unidiff_patch = (
    "Index: iota\n"
    "===================================================================\n"
    "diff --git a/iota b/iota\n"
    "old mode 100644\n"
    "new mode 100755\n"
    "Property changes on: iota\n"
    "-------------------------------------------------------------------\n"
    "Added: svn:executable\n"
    "## -0,0 +1 ##\n"
    "+*\n"
    )
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, unidiff_patch)

  expected_output = [
    ' U        %s\n' % sbox.ospath('iota'),
  ]

  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota', props={'svn:executable': '*'})

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', status=' M')

  expected_skip = wc.State('', { })

  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       error_re_string=None,
                                       check_props=True)

def patch_prop_madness(sbox):
  "patch property madness"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_propset('mod_s', 'value\n',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_s_n', 'no-eol',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_l', 'this\nis\na\nvery\nvery\nlong\nvalue.\n',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_l_n', 'this\nis\na\nvery\nvery\nlong\nvalue.\n'
                      'without\neol', # No eol at end
                      'iota', 'A/mu')

  sbox.simple_propset('del', 'value\n',
                      'iota', 'A/mu')

  sbox.simple_propset('del_n', 'no-eol',
                      'iota', 'A/mu')

  sbox.simple_commit()

  r2_props = {
   'mod_l_n' : 'this\nis\na\nvery\nvery\nlong\nvalue.\nwithout\neol',
   'mod_l'   : 'this\nis\na\nvery\nvery\nlong\nvalue.\n',
   'mod_s'   : 'value\n',
   'mod_s_n' : 'no-eol',
   'del'     : 'value\n',
   'del_n'   : 'no-eol',
  }
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota', 'A/mu', props=r2_props)

  sbox.simple_propset('mod_s', 'other\n',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_s_n', 'still no eol',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_l', 'this\nis\na\nsomewhat\nlong\nvalue.\n',
                      'iota', 'A/mu')

  sbox.simple_propset('mod_l_n', 'this\nis\na\nanother\n..\nlong\nvalue.\n'
                      'without\neol', # No eol at end
                      'iota', 'A/mu')

  sbox.simple_propdel('del', 'iota', 'A/mu')

  sbox.simple_propdel('del_n', 'iota', 'A/mu')

  sbox.simple_propset('add_s', 'new-value\n',
                      'iota', 'A/mu')

  sbox.simple_propset('add_s_n', 'new other no eol',
                      'iota', 'A/mu')

  sbox.simple_propset('add_l', 'this\nis\nsomething\n',
                      'iota', 'A/mu')

  sbox.simple_propset('add_l_n', 'this\nhas\nno\neol', # No eol at end
                      'iota', 'A/mu')

  _, output, _ = svntest.actions.run_and_verify_svn(None, [],
                                                    'diff', wc_dir)

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)

  new_props = {
    'mod_s'       : 'other\n',
    'mod_s_n'     : 'still no eol',
    'mod_l'       : 'this\nis\na\nsomewhat\nlong\nvalue.\n',
    'mod_l_n'     : 'this\nis\na\nanother\n..\nlong\nvalue.\nwithout\neol',
    'add_s'       : 'new-value\n',
    'add_s_n'     : 'new other no eol',
    'add_l'       : 'this\nis\nsomething\n',
    'add_l_n'     : 'this\nhas\nno\neol'
  }

  expected_status.tweak('iota', 'A/mu', status=' M', wc_rev='2')
  expected_disk.tweak('iota', 'A/mu', props=new_props)

  svntest.actions.verify_disk(wc_dir, expected_disk, True)
  #svntest.actions.run_and_verify_status(wc_dir, expected_status)

  svntest.actions.run_and_verify_svn(None, [],
                                     'revert', wc_dir, '-R')

  patch = sbox.get_tempname('patch')
  svntest.main.file_write(patch, ''.join(output), mode='wb')

  expected_output = wc.State(wc_dir, {
    'A/mu' : Item(status=' U'),
    'iota' : Item(status=' U'),
  })
  expected_skip= wc.State(wc_dir, {
  })

  strip_count = wc_dir.count(os.path.sep)+1

  # Patch once
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # Patch again
  expected_output.tweak('A/mu', 'iota', status=' G')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # Reverse
  expected_output.tweak('A/mu', 'iota', status=' U')
  expected_disk.tweak('A/mu', 'iota', props=r2_props)
  expected_status.tweak('A/mu', 'iota', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff',
                                       '--strip', strip_count)

  # And repeat
  expected_output.tweak('A/mu', 'iota', status=' G')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff',
                                       '--strip', strip_count)

  # Ok, and now introduce some conflicts

  sbox.simple_propset('del', 'value', 'iota') # Wrong EOL
  sbox.simple_propset('del_n', 'regeleinde\n', 'iota') # Wrong EOL+value

  sbox.simple_propset('del', 'waarde', 'A/mu') # Wrong EOL+value
  sbox.simple_propset('del_n', 'no-eol\n', 'A/mu') # Wrong EOL

  expected_output.tweak('A/mu', 'iota', status=' C')
  expected_status.tweak('iota', 'A/mu', status=' M')

  iota_props = new_props.copy()
  iota_props['del_n'] = 'regeleinde\n'
  mu_props = new_props.copy()
  mu_props['del'] = 'waarde'
  expected_disk.tweak('iota', props=iota_props)
  expected_disk.tweak('A/mu', props=mu_props)

  expected_disk.add({
   'A/mu.svnpatch.rej' : Item(contents="--- %s\n"
                                       "+++ %s\n"
                                       "Property: del\n"
                                       "## -1,1 +0,0 ##\n"
                                       "-value\n"
                                       % (sbox.path('A/mu'),
                                          sbox.path('A/mu'))),
   'iota.svnpatch.rej' : Item(contents="--- %s\n"
                                       "+++ %s\n"
                                       "Property: del_n\n"
                                       "## -1,1 +0,0 ##\n"
                                       "-no-eol\n"
                                       "\ No newline at end of property\n"
                                       % (sbox.path('iota'),
                                          sbox.path('iota'))),
  })

  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

def patch_empty_vs_delete(sbox):
  "patch empty vs delete"

  sbox.build(read_only = True)
  wc_dir = sbox.wc_dir
  strip_count = wc_dir.count(os.path.sep)+1

  sbox.simple_append('iota', '', truncate=True)

  _, empty_diff, _ = svntest.actions.run_and_verify_svn(None, [],
                                                        'diff', wc_dir)

  _, empty_git, _ = svntest.actions.run_and_verify_svn(None, [],
                                                       'diff', wc_dir, '--git')

  svntest.actions.run_and_verify_svn(None, [],
                                     'rm', '--force', sbox.ospath('iota'))

  _, del_diff, _ = svntest.actions.run_and_verify_svn(None, [],
                                                      'diff', wc_dir)

  _, del_git, _ = svntest.actions.run_and_verify_svn(None, [],
                                                     'diff', wc_dir, '--git')

  empty_patch = sbox.get_tempname('empty.patch')
  svntest.main.file_write(empty_patch, ''.join(empty_diff), mode='wb')

  empty_git_patch = sbox.get_tempname('git.empty.patch')
  svntest.main.file_write(empty_git_patch, ''.join(empty_git), mode='wb')

  del_patch = sbox.get_tempname('del.patch')
  svntest.main.file_write(del_patch, ''.join(del_diff), mode='wb')

  del_git_patch = sbox.get_tempname('git.del.patch')
  svntest.main.file_write(del_git_patch, ''.join(del_git), mode='wb')

  svntest.actions.run_and_verify_svn(None, [],
                                     'revert', sbox.ospath('iota'))

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_disk = svntest.main.greek_state.copy()
  expected_skip = svntest.wc.State(wc_dir, {})


  # Git diff to empty file - Expect empty file
  expected_output = svntest.wc.State(wc_dir, {
    'iota' : Item(status='U ')
  })
  expected_disk.tweak('iota', contents='')
  expected_status.tweak('iota', status='M ')
  svntest.actions.run_and_verify_patch(wc_dir, empty_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, empty_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  svntest.actions.run_and_verify_svn(None, [],
                                     'revert', sbox.ospath('iota'))

  # Ordinary (unified) diff to empty file - Expect deleted
  expected_output = svntest.wc.State(wc_dir, {
    'iota' : Item(status='D ')
  })
  expected_disk.remove('iota')
  expected_status.tweak('iota', status='D ')

  svntest.actions.run_and_verify_patch(wc_dir, empty_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # Retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, empty_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  svntest.actions.run_and_verify_svn(None, [],
                                     'revert', sbox.ospath('iota'))

  # Ordinary diff to deleted
  expected_output.tweak('iota', status='D ')
  svntest.actions.run_and_verify_patch(wc_dir, del_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # Retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, del_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  svntest.actions.run_and_verify_svn(None, [],
                                     'revert', sbox.ospath('iota'))

  # Git diff to deleted
  expected_output.tweak('iota', status='D ')
  svntest.actions.run_and_verify_patch(wc_dir, del_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, del_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # # Not needed. Result of previous test
  #svntest.actions.run_and_verify_svn(None, [],
  #                                   'rm', '--force', sbox.ospath('iota'))

  # Ok, and now let's check what happens on reverse diffs with nothing
  # there

  # Git empty patch -> skip... target not found
  expect_no_output = svntest.wc.State(wc_dir, {})
  expect_skip_iota = svntest.wc.State(wc_dir, {
    'iota' : Item(verb='Skipped')
  })
  svntest.actions.run_and_verify_patch(wc_dir, empty_git_patch,
                                       expect_no_output, expected_disk,
                                       expected_status, expect_skip_iota,
                                       [], True, True,
                                       '--reverse-diff')

  # # Not needed. Result of previous test
  #svntest.actions.run_and_verify_svn(None, [],
  #                                   'rm', '--force', sbox.ospath('iota'))

  # Unified empty patch -> Create iota
  expected_output.tweak('iota', status='A ')
  expected_status.tweak('iota', status='R ')
  expected_disk.add({
    'iota' : Item(contents="This is the file 'iota'.\n")
  })
  svntest.actions.run_and_verify_patch(wc_dir, empty_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')
  # And retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, empty_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')

  svntest.actions.run_and_verify_svn(None, [],
                                     'rm', '--force', sbox.ospath('iota'))

  expected_output.tweak('iota', status='A ')
  svntest.actions.run_and_verify_patch(wc_dir, del_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')
  # And retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, del_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')

  svntest.actions.run_and_verify_svn(None, [],
                                     'rm', '--force', sbox.ospath('iota'))

  expected_output.tweak('iota', status='A ')
  svntest.actions.run_and_verify_patch(wc_dir, del_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')
  # And retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, del_git_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

def patch_add_remove_executable(sbox):
  "add and remove executable file"

  sbox.build()
  wc_dir = sbox.wc_dir

  eicar_data = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$' \
               'EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\0'
  other_data = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$' \
               'SOME-LESS-INTERESTING-OTHER-TEXT!!!$H+H*\0' \
               '\0\0\0\0\0\0\0\0'

  # Write out an actual MS-DOS program
  sbox.simple_add_text(eicar_data, 'eicar.com')
  sbox.simple_propset('svn:executable', 'x', 'eicar.com')

  _, diff_add, _ = svntest.actions.run_and_verify_svn(None, [],
                                                      'diff', '--git', wc_dir)

  sbox.simple_commit()

  sbox.simple_append('eicar.com', other_data, truncate=True)
  sbox.simple_propdel('svn:executable', 'eicar.com')

  _, diff_edit, _ = svntest.actions.run_and_verify_svn(None, [],
                                                       'diff', '--git', wc_dir)

  sbox.simple_commit()
  sbox.simple_rm('eicar.com')

  _, diff_rm, _ = svntest.actions.run_and_verify_svn(None, [],
                                                     'diff', '--git', wc_dir)

  add_patch = sbox.get_tempname('add.patch')
  svntest.main.file_write(add_patch, ''.join(diff_add), mode='wb')

  edit_patch = sbox.get_tempname('edit.patch')
  svntest.main.file_write(edit_patch, ''.join(diff_edit), mode='wb')

  rm_patch = sbox.get_tempname('rm.patch')
  svntest.main.file_write(rm_patch, ''.join(diff_rm), mode='wb')

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'eicar.com' : Item(status='RM', wc_rev=3)
  })
  expected_output = svntest.wc.State(wc_dir, {
    'eicar.com' : Item(status='A ')
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'eicar.com' : Item(contents=eicar_data,
                       props={'svn:mime-type': 'application/octet-stream',
                              'svn:executable': '*'}),
  })
  expected_skip = svntest.wc.State(wc_dir, {})
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Now apply the edit
  expected_output.tweak('eicar.com', status='UU')
  expected_disk.tweak('eicar.com',
                      props={'svn:mime-type': 'application/octet-stream'},
                      contents=other_data)
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Now apply the edit
  expected_output.tweak('eicar.com', status='D ')
  expected_disk.remove('eicar.com')
  expected_status.tweak('eicar.com', status='D ')
  svntest.actions.run_and_verify_patch(wc_dir, rm_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, rm_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  #And reverse
  expected_output.tweak('eicar.com', status='A ')
  expected_disk.add({
    'eicar.com' : Item(contents=other_data,
                       props={'svn:mime-type': 'application/octet-stream'}),
  })
  expected_status.tweak('eicar.com', status='RM')
  svntest.actions.run_and_verify_patch(wc_dir, rm_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, rm_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And reverse the edit
  expected_output.tweak('eicar.com', status='UU')
  expected_disk.tweak('eicar.com', contents=eicar_data,
                      props={'svn:mime-type': 'application/octet-stream',
                              'svn:executable': '*'})
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')
  # Repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And the add
  expected_output.tweak('eicar.com', status='D ')
  expected_disk.remove('eicar.com')
  expected_status.tweak('eicar.com', status='D ')
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And a final repeat
  expected_output.tweak('eicar.com', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

def patch_git_symlink(sbox):
  "patch a git symlink"

  sbox.build(read_only = True)
  wc_dir = sbox.wc_dir

  patch_add = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'new file mode 120000\n',
    'index 0000000..3ef26e4\n',
    '--- /dev/null\n',
    '+++ b/link-to-iota\n',
    '@@ -0,0 +1 @@\n',
    '+iota\n',
    '\ No newline at end of file\n',
  ]

  patch_edit = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'index 3ef26e4..33e5b38 120000\n',
    '--- a/link-to-iota\n',
    '+++ b/link-to-iota\n',
    '@@ -1 +1 @@\n',
    '-iota\n',
    '\ No newline at end of file\n',
    '+A/mu\n',
    '\ No newline at end of file\n',
  ]

  patch_to_file = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'deleted file mode 120000\n',
    'index 33e5b38..0000000\n',
    '--- a/link-to-iota\n',
    '+++ /dev/null\n',
    '@@ -1 +0,0 @@\n',
    '-A/mu\n',
    '\ No newline at end of file\n',
    'diff --git a/link-to-iota b/link-to-iota\n',
    'new file mode 100644\n',
    'index 0000000..1b130bf\n',
    '--- /dev/null\n',
    '+++ b/link-to-iota\n',
    '@@ -0,0 +1 @@\n',
    '+This is a real file\n',
  ]

  add_patch = sbox.get_tempname('add.patch')
  svntest.main.file_write(add_patch, ''.join(patch_add), mode='wb')

  edit_patch = sbox.get_tempname('edit.patch')
  svntest.main.file_write(edit_patch, ''.join(patch_edit), mode='wb')

  to_file_patch = sbox.get_tempname('to_file.patch')
  svntest.main.file_write(to_file_patch, ''.join(patch_to_file), mode='wb')


  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'link-to-iota'      : Item(status='A ', wc_rev='-'),
  })
  expected_output = svntest.wc.State(wc_dir, {
    'link-to-iota'      : Item(status='A '),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'link-to-iota'      : Item(contents="This is the file 'iota'.\n",
                               props={'svn:special': '*'}),
  })
  if not svntest.main.is_posix_os():
    expected_disk.tweak('link-to-iota', contents='link iota')
  expected_skip = svntest.wc.State(wc_dir, {})

  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again
  expected_output.tweak('link-to-iota', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Now tweak the link
  expected_output.tweak('link-to-iota', status='U ')
  if svntest.main.is_posix_os():
    expected_disk.tweak('link-to-iota', contents="This is the file 'mu'.\n")
  else:
    expected_disk.tweak('link-to-iota', contents='link A/mu')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again
  expected_output.tweak('link-to-iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And replace the link with a file
  expected_output.tweak('link-to-iota', status='A ', prev_status='D ')
  expected_disk.tweak('link-to-iota', contents="This is a real file\n",
                      props={})
  svntest.actions.run_and_verify_patch(wc_dir, to_file_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again - Delete can't be applied
  expected_output.tweak('link-to-iota', status='G ', prev_status='C ')
  expected_disk.add({
    'link-to-iota.svnpatch.rej': Item(
                     contents='--- link-to-iota\n'
                              '+++ /dev/null\n'
                              '@@ -1,1 +0,0 @@\n'
                              '-A/mu\n'
                              '\\ No newline at end of file\n'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, to_file_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

def patch_like_git_symlink(sbox):
  "patch like a git symlink"

  sbox.build(read_only = True)
  wc_dir = sbox.wc_dir

  patch_add = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'new file mode 100000\n',
    'index 0000000..3ef26e4\n',
    '--- /dev/null\n',
    '+++ b/link-to-iota\n',
    '@@ -0,0 +1 @@\n',
    '+iota\n',
    '\ No newline at end of file\n',
  ]

  patch_edit = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'index 3ef26e4..33e5b38 100000\n',
    '--- a/link-to-iota\n',
    '+++ b/link-to-iota\n',
    '@@ -1 +1 @@\n',
    '-iota\n',
    '\ No newline at end of file\n',
    '+A/mu\n',
    '\ No newline at end of file\n',
  ]

  patch_to_file = [
    'diff --git a/link-to-iota b/link-to-iota\n',
    'deleted file mode 100000\n',
    'index 33e5b38..0000000\n',
    '--- a/link-to-iota\n',
    '+++ /dev/null\n',
    '@@ -1 +0,0 @@\n',
    '-A/mu\n',
    '\ No newline at end of file\n',
    'diff --git a/link-to-iota b/link-to-iota\n',
    'new file mode 100644\n',
    'index 0000000..1b130bf\n',
    '--- /dev/null\n',
    '+++ b/link-to-iota\n',
    '@@ -0,0 +1 @@\n',
    '+This is a real file\n',
  ]

  add_patch = sbox.get_tempname('add.patch')
  svntest.main.file_write(add_patch, ''.join(patch_add), mode='wb')

  edit_patch = sbox.get_tempname('edit.patch')
  svntest.main.file_write(edit_patch, ''.join(patch_edit), mode='wb')

  to_file_patch = sbox.get_tempname('to_file.patch')
  svntest.main.file_write(to_file_patch, ''.join(patch_to_file), mode='wb')

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'link-to-iota'      : Item(status='A ', wc_rev='-'),
  })
  expected_output = svntest.wc.State(wc_dir, {
    'link-to-iota'      : Item(status='A '),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'link-to-iota'      : Item(contents="iota"),
  })
  expected_skip = svntest.wc.State(wc_dir, {})

  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again
  expected_output.tweak('link-to-iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, add_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Now tweak the link
  expected_output.tweak('link-to-iota', status='U ')
  expected_disk.tweak('link-to-iota', contents='A/mu')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again
  expected_output.tweak('link-to-iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, edit_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And replace the link with a file
  expected_output.tweak('link-to-iota', status='U ')
  expected_output.tweak('link-to-iota', status='A ', prev_status='D ')
  expected_disk.tweak('link-to-iota', contents="This is a real file\n")
  svntest.actions.run_and_verify_patch(wc_dir, to_file_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And again - Delete can't be applied
  expected_output.tweak('link-to-iota', status='G ', prev_status='C ')
  expected_disk.add({
    'link-to-iota.svnpatch.rej': Item(
                     contents='--- link-to-iota\n'
                              '+++ /dev/null\n'
                              '@@ -1,1 +0,0 @@\n'
                              '-A/mu\n'
                              '\\ No newline at end of file\n'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, to_file_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

def patch_symlink_changes(sbox):
  "patch symlink changes"

  sbox.build()
  wc_dir = sbox.wc_dir
  strip_count = wc_dir.count(os.path.sep)+1

  os.remove(sbox.ospath('iota'))
  sbox.simple_symlink('A/B/E/beta', 'iota')
  sbox.simple_propset('svn:special', 'X', 'iota')

  _, diff_tolink, _ = svntest.actions.run_and_verify_svn(None, [],
                                                         'diff', wc_dir)

  _, git_tolink, _ = svntest.actions.run_and_verify_svn(None, [],
                                                         'diff', wc_dir, '--git')

  sbox.simple_commit()

  os.remove(sbox.ospath('iota'))
  sbox.simple_symlink('A/B/E/alpha', 'iota')

  _, diff_changelink, _ = svntest.actions.run_and_verify_svn(None, [],
                                                            'diff', wc_dir)

  _, git_changelink, _ = svntest.actions.run_and_verify_svn(None, [],
                                                            'diff', wc_dir, '--git')

  tolink_patch = sbox.get_tempname('tolink.patch')
  svntest.main.file_write(tolink_patch, ''.join(diff_tolink), mode='wb')

  git_tolink_patch = sbox.get_tempname('git_tolink.patch')
  svntest.main.file_write(git_tolink_patch, ''.join(git_tolink), mode='wb')

  changelink_patch = sbox.get_tempname('changelink.patch')
  svntest.main.file_write(changelink_patch, ''.join(diff_changelink), mode='wb')

  git_changelink_patch = sbox.get_tempname('git_changelink.patch')
  svntest.main.file_write(git_changelink_patch, ''.join(git_changelink), mode='wb')

  sbox.simple_revert('iota')
  sbox.simple_update('', 1)

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('iota', status='MM')
  expected_output = svntest.wc.State(wc_dir, {
    'iota'      : Item(status='UU'),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('iota', props={'svn:special': '*'})
  expected_skip = svntest.wc.State(wc_dir, {})

  if svntest.main.is_posix_os():
    expected_disk.tweak('iota', contents="This is the file 'beta'.\n")
  else:
    expected_disk.tweak('iota', contents="link A/B/E/beta")

  # Turn into link
  svntest.actions.run_and_verify_patch(wc_dir, tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # And in git style
  sbox.simple_revert('iota')
  svntest.actions.run_and_verify_patch(wc_dir, git_tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output.tweak('iota', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)
  svntest.actions.run_and_verify_patch(wc_dir, git_tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  sbox.simple_update('', 2) # Go to r2.
  sbox.simple_revert('iota')
  expected_status.tweak(wc_rev=2)

  # Turn back into files
  expected_output.tweak('iota', status='UU')
  expected_disk.tweak('iota', props={}, contents="This is the file 'iota'.\n")
  svntest.actions.run_and_verify_patch(wc_dir, tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')

  # And in git style
  sbox.simple_revert('iota')
  svntest.actions.run_and_verify_patch(wc_dir, git_tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Retry
  expected_output.tweak('iota', status='GG')
  svntest.actions.run_and_verify_patch(wc_dir, tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count,
                                       '--reverse-diff')
  svntest.actions.run_and_verify_patch(wc_dir, git_tolink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And now just tweak the link
  expected_output.tweak('iota', status='U ')
  expected_disk.tweak('iota', props={'svn:special': '*'})
  expected_status.tweak('iota', status='M ')

  if svntest.main.is_posix_os():
    expected_disk.tweak('iota', contents="This is the file 'alpha'.\n")
  else:
    expected_disk.tweak('iota', contents="link A/B/E/alpha")

  sbox.simple_revert('iota')
  svntest.actions.run_and_verify_patch(wc_dir, changelink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

  # And in git style
  sbox.simple_revert('iota')
  svntest.actions.run_and_verify_patch(wc_dir, git_changelink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output.tweak('iota', status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, changelink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)
  svntest.actions.run_and_verify_patch(wc_dir, git_changelink_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

def patch_add_one_line(sbox):
  "patch add just one line"

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  diff = [
    # This is a normal unified diff
    "Index: A/B/E/alpha",
    "===================================================================",
    "--- A/B/E/alpha\t(revision 1)",
    "+++ A/B/E/alpha\t(working copy)",
    "@@ -1 +1,2 @@",
    " This is the file 'alpha'.",
    "+This is the file 'alpha'.",

    "",

    # This diff is hand crafted, as a generated diff would add the line at
    # the end
    "Index: A/B/E/beta",
    "===================================================================",
    "--- A/B/E/beta\t(revision 1)",
    "+++ A/B/E/beta\t(working copy)",
    "@@ -1 +1,2 @@",
    "+This is the file 'beta'.",
    " This is the file 'beta'.",
    ""
  ]

  recurse_patch = sbox.get_tempname('recurse.patch')
  svntest.main.file_write(recurse_patch, '\n'.join(diff), mode='wb')

  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('A/B/E/alpha', 'A/B/E/beta', status='M ')
  expected_output = svntest.wc.State(wc_dir, {
    'A/B/E/alpha'   : Item(status='U '),
    'A/B/E/beta'    : Item(status='U '),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('A/B/E/alpha', contents="This is the file 'alpha'.\nThis is the file 'alpha'.\n")
  expected_disk.tweak('A/B/E/beta', contents="This is the file 'beta'.\nThis is the file 'beta'.\n")
  expected_skip = svntest.wc.State(wc_dir, {})

  svntest.actions.run_and_verify_patch(wc_dir, recurse_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output.tweak(status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, recurse_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  sbox.simple_append('A/B/E/alpha',
                     "This is the file 'alpha'.\n")
  sbox.simple_append('A/B/E/beta',
                     "This is the file 'beta'.\n")

  # But can we remove the line? - Yes
  expected_output.tweak(status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, recurse_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Once more?
  expected_disk = svntest.main.greek_state.copy()
  expected_status.tweak('A/B/E/alpha', 'A/B/E/beta', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, recurse_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # And the last lines? - No...
  expected_output.tweak(status='G ')
  svntest.actions.run_and_verify_patch(wc_dir, recurse_patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

def patch_with_mergeinfo(sbox):
  "patch with mergeinfo"

  sbox.build()
  wc_dir = sbox.wc_dir
  strip_count = wc_dir.count(os.path.sep)+1

  sbox.simple_copy('A/B/E', 'E')
  sbox.simple_append('A/B/E/alpha', 'extra\nlines\n')
  sbox.simple_commit()

  sbox.simple_propset('a', 'A', 'E') # 'a' < 'svn:mergeinfo'
  sbox.simple_propset('z', 'Z', 'E') # 'z' > 'svn:mergeinfo'

  svntest.actions.run_and_verify_svn(None, [],
                                     'merge', '^/A/B/E', sbox.ospath('E'))

  _, diff, _ = svntest.actions.run_and_verify_svn(None, [],
                                                  'diff', wc_dir)

  sbox.simple_revert('E', 'E/alpha')

  patch = sbox.get_tempname('recurse.patch')
  svntest.main.file_write(patch, ''.join(diff), mode='wb')

  expected_output = wc.State(wc_dir, {
    'E'                 : Item(status=' U'),
    'E/alpha'           : Item(status='U '),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'E'                 : Item(status=' M', wc_rev='2'),
    'E/alpha'           : Item(status='M ', wc_rev='2'),
    'E/beta'            : Item(status='  ', wc_rev='2'),
  })
  expected_status.tweak('A/B/E/alpha', wc_rev=2)
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('A/B/E/alpha', contents="This is the file 'alpha'.\nextra\nlines\n")
  expected_disk.add({
    'E'                 : Item(props={'a': 'A',
                                      # We can't apply 'svn:mergeinfo' (yet)
                                      'z': 'Z'}),
    'E/beta'            : Item(contents="This is the file 'beta'.\n"),
    'E/alpha'           : Item(contents="This is the file 'alpha'.\nextra\nlines\n"),
  })

  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--strip', strip_count)

def patch_move_and_change(sbox):
  "patch move and change"

  sbox.build(read_only = True)
  wc_dir = sbox.wc_dir

  sbox.simple_append('A/B/E/alpha', 'extra\nlines\n')
  sbox.simple_propset('k', 'v', 'A/B/E/alpha')

  sbox.simple_move('A/B/E/alpha', 'alpha')

  _, diff, _ = svntest.actions.run_and_verify_svn(None, [],
                                                  'diff', wc_dir, '--git')

  patch = sbox.get_tempname('move_and_change.patch')
  svntest.main.file_write(patch, ''.join(diff), mode='wb')

  # Running the diff reversed doesn't work...
  # We perform the add before reverting the move...
  expected_output = wc.State(wc_dir, {
    'A/B/E/alpha' : Item(status='A '),
  })
  expected_skip = wc.State(wc_dir, {
    'alpha' : Item(verb='Skipped'),
  })
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.tweak('A/B/E/alpha', status='R ',
                        moved_to='alpha')
  expected_status.add({
    'alpha'             : Item(status='A ', copied='+',
                               moved_from='A/B/E/alpha', wc_rev='-'),
  })
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'alpha' : Item(contents="This is the file 'alpha'.\nextra\nlines\n",
                   props={'k': 'v'}),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

  # Ok, let's remove the 'delete' portion and try in a clean WC
  n = diff.index('Index: %s\n' % sbox.path('alpha'))
  diff = diff[n:]
  svntest.main.file_write(patch, ''.join(diff), mode='wb')

  sbox.simple_revert('A/B/E/alpha', 'alpha')

  expected_output = wc.State(wc_dir, {
    'A/B/E/alpha' : Item(status='D '),
    'alpha'       : Item(status='A '),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_disk.remove('A/B/E/alpha')
  expected_status.tweak('A/B/E/alpha', status='D ')
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # Retry
  expected_output = svntest.wc.State(wc_dir, {
    'alpha'             : Item(status='GG'),
  })
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True)

  # And now reverse
  expected_output = wc.State(wc_dir, {
    'alpha'       : Item(status='D '),
    'A/B/E/alpha' : Item(status='A '),
  })
  expected_disk.remove('alpha')
  expected_disk.add({
    'A/B/E/alpha'       : Item(contents="This is the file 'alpha'.\n"),
  })
  expected_status.remove('alpha')
  expected_status.tweak('A/B/E/alpha', status='  ', moved_to=None)
  svntest.actions.run_and_verify_patch(wc_dir, patch,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], True, True,
                                       '--reverse-diff')

@Issue(4609)
def missing_trailing_context(sbox):
  "missing trailing context"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_append('A/mu',
                     'a\n'
                     'b\n'
                     'c\n'
                     'd\n'
                     'e\n',
                     truncate=True)
  sbox.simple_commit()
  sbox.simple_update()

  # The hunk is expected to have two lines of trailing context but
  # only has one.
  unidiff_patch = [
    "Index: A/mu\n"
    "===================================================================\n",
    "--- A/mu\t(revision 2)\n",
    "+++ A/mu\t(working copy)\n",
    "@@ -1,5 +1,5 @@\n",
    " a\n",
    " b\n",
    "-c\n",
    "+cc\n",
    " d\n",
  ]
  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, ''.join(unidiff_patch), 'wb')

  # GNU patch will apply the hunk with fuzz 1 and modify only the 'c' line.
  # Our patch file finds the length mismatch and applies a penalty.
  expected_output = [
    'U         %s\n' % sbox.ospath('A/mu'),
    '>         applied hunk @@ -1,4 +1,4 @@ with fuzz 1\n',
  ]
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.tweak('A/mu', contents =
                     'a\n'
                     'b\n'
                     'cc\n'
                     'd\n'
                     'e\n')
  expected_status = svntest.actions.get_virginal_state(wc_dir, 2)
  expected_status.tweak('A/mu', status='M ')
  expected_skip = wc.State('', { })
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)

  # Try reverse patch
  expected_disk.tweak('A/mu', contents =
                     'a\n'
                     'b\n'
                     'c\n'
                     'd\n'
                     'e\n')
  expected_status.tweak('A/mu', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

  # The hunk is expected to have two lines of trailing context but
  # only has one.
  unidiff_patch = [
    "Index: A/mu\n"
    "===================================================================\n",
    "--- A/mu\t(revision 2)\n",
    "+++ A/mu\t(working copy)\n",
    "@@ -1,4 +1,4 @@\n",
    " a\n",
    " b\n",
    "-c\n",
    "+cc\n",
    " d\n",
    " e\n",
  ]
  patch_file_path = sbox.get_tempname('my2.patch')
  svntest.main.file_write(patch_file_path, ''.join(unidiff_patch), 'wb')

  expected_output = [
    'U         %s\n' % sbox.ospath('A/mu'),
    '>         applied hunk @@ -1,5 +1,5 @@ with fuzz 1\n',
  ]
  expected_disk.tweak('A/mu', contents =
                     'a\n'
                     'b\n'
                     'cc\n'
                     'd\n'
                     'e\n')
  expected_status.tweak('A/mu', status='M ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)

  # Try reverse patch
  expected_disk.tweak('A/mu', contents =
                     'a\n'
                     'b\n'
                     'c\n'
                     'd\n'
                     'e\n')
  expected_status.tweak('A/mu', status='  ')
  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip,
                                       [], False, True, '--reverse-diff')

def patch_missed_trail(sbox):
  "apply a patch to an empty file"

  sbox.build()
  wc_dir = sbox.wc_dir

  patch_file_path = sbox.get_tempname('my.patch')
  svntest.main.file_write(patch_file_path, ''.join([
  # Add a line to a file with just '\n' with bad header (should be +1,2)
    "Index: lf.txt\n",
    "===================================================================\n",
    "--- lf.txt\t(revision 2)\n",
    "+++ lf.txt\t(working copy)\n",
    "@@ -1 +1 @@\n",
    "\n"
    "+replacement\n",
  ]))

  sbox.simple_add_text('\n', 'lf.txt')
  sbox.simple_commit()

  expected_output = [
    'U         %s\n' % sbox.ospath('lf.txt'),
    '>         applied hunk @@ -1,1 +1,2 @@ with fuzz 1\n',
  ]

  # Current result: lf.txt patched ok, new created, empty succeeds with offset.
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'lf.txt'            : Item(contents="\nreplacement\n"),
  })
  expected_skip = wc.State(wc_dir, {})
  expected_status = None

  svntest.actions.run_and_verify_patch(wc_dir, patch_file_path,
                                       expected_output, expected_disk,
                                       expected_status, expected_skip)

def patch_merge(sbox):
  "patching a specific merge"

  sbox.build()
  wc_dir = sbox.wc_dir
  repo_url = sbox.repo_url

  sbox.simple_add_text('A\n'
                       'B\n'
                       'C\n'
                       'J\n'
                       'K\n'
                       'L', 'new.txt')
  sbox.simple_commit()

  remote_patch = sbox.get_tempname('remote.patch')
  svntest.main.file_write(remote_patch,
      '--- new.txt\t(revision 6)\n'
      '+++ new.txt\t(revision 7)\n'
      '@@ -1,6 +1,9 @@\n'
      ' A\n'
      ' B\n'
      '-C\n'
      '+ C\n'
      '+D\n'
      '+E\n'
      '+F\n'
      ' J\n'
      ' K\n'
      ' L\n'
      '\ No newline at end of file', mode='wb')

  expected_skip = wc.State('', { })
  expected_output = wc.State(wc_dir, {
      'new.txt' : Item(status='U '),
    })
  svntest.actions.run_and_verify_patch(wc_dir, remote_patch,
                                       expected_output, None,
                                       None, expected_skip)
  sbox.simple_commit()
  sbox.simple_update(revision=2)

  local_patch = sbox.get_tempname('local.patch')
  svntest.main.file_write(local_patch,
      '--- new.txt\t(revision 3)\n'
      '+++ new.txt\t(revision 4)\n'
      '@@ -1,6 +1,9 @@\n'
      ' A\n'
      ' B\n'
      ' C\n'
      '+D\n'
      '+E\n'
      '+F\n'
      ' J\n'
      ' K\n'
      ' L\n'
      '\ No newline at end of file', mode='wb')

  svntest.actions.run_and_verify_patch(wc_dir, local_patch,
                                       expected_output, None,
                                       None, expected_skip)

  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'new.txt' : Item(contents='A\n'
                              'B\n'
                              '<<<<<<< .mine\n'
                              'C\n'
                              'D\n'
                              'E\n'
                              'F\n'
                              '||||||| .r2\n'
                              'C\n'
                              '=======\n'
                             ' C\n'
                             'D\n'
                             'E\n'
                             'F\n'
                             '>>>>>>> .r3\n'
                             'J\n'
                             'K\n'
                             'L'),
    'new.txt.mine'      : Item(contents="A\nB\nC\nD\nE\nF\nJ\nK\nL"),
    'new.txt.r2'        : Item(contents="A\nB\nC\nJ\nK\nL"),
    'new.txt.r3'        : Item(contents="A\nB\n C\nD\nE\nF\nJ\nK\nL"),
  })
  expected_output.tweak('new.txt', status='C ')
  svntest.actions.run_and_verify_update(wc_dir, expected_output, expected_disk,
                                        None, [])

  # Revert to base position
  sbox.simple_revert('new.txt')
  sbox.simple_update(revision=2)

  # And now do the same thing as a merge instead of an update
  expected_output.tweak('new.txt', status='U ')
  svntest.actions.run_and_verify_patch(wc_dir, local_patch,
                                       expected_output, None,
                                       None, expected_skip)

  expected_output.tweak('new.txt', status='C ')
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.add({
    'new.txt' : Item(contents='A\n'
                              'B\n'
                              '<<<<<<< .working\n'
                              'C\n'
                              'D\n'
                              'E\n'
                              'F\n'
                              '||||||| .merge-left.r2\n'
                              'C\n'
                              '=======\n'
                             ' C\n'
                             'D\n'
                             'E\n'
                             'F\n'
                             '>>>>>>> .merge-right.r3\n'
                             'J\n'
                             'K\n'
                             'L'),
    'new.txt.working'        : Item(contents="A\nB\nC\nD\nE\nF\nJ\nK\nL"),
    'new.txt.merge-left.r2'  : Item(contents="A\nB\nC\nJ\nK\nL"),
    'new.txt.merge-right.r3' : Item(contents="A\nB\n C\nD\nE\nF\nJ\nK\nL"),
  })

  svntest.actions.run_and_verify_merge(wc_dir, 2, 3, repo_url, repo_url,
                                       expected_output, None, None,
                                       expected_disk, None,
                                       expected_skip)

              patch_symlink_traversal,
              patch_obstructing_symlink_traversal,
              patch_binary_file,
              patch_delete_nodes,
              patch_delete_missing_eol,
              patch_final_eol,
              patch_adds_executability_nocontents,
              patch_adds_executability_nocontents2,
              patch_adds_executability_yescontents,
              patch_deletes_executability,
              patch_ambiguous_executability_contradiction,
              patch_ambiguous_executability_consistent,
              patch_prop_madness,
              patch_empty_vs_delete,
              patch_add_remove_executable,
              patch_git_symlink,
              patch_like_git_symlink,
              patch_symlink_changes,
              patch_add_one_line,
              patch_with_mergeinfo,
              patch_move_and_change,
              missing_trailing_context,
              patch_missed_trail,
              patch_merge,
import command
import gitutil
import terminal
def CheckPatch(fname, verbose=False):
    result.errors, result.warning, result.checks = 0, 0, 0
    result.stdout = command.Output(chk, '--no-tree', fname,
                                   raise_on_error=False)
    re_stats = re.compile('total: (\\d+) errors, (\d+) warnings, (\d+)')
    re_stats_full = re.compile('total: (\\d+) errors, (\d+) warnings, (\d+)'
    re_error = re.compile('ERROR: (.*)')
    re_warning = re.compile('WARNING: (.*)')
    re_check = re.compile('CHECK: (.*)')
    re_file = re.compile('#\d+: FILE: ([^:]*):(\d+):')

        if not line and item:
            result.problems.append(item)
            item = {}
            item['msg'] = err_match.group(1)
            item['msg'] = warn_match.group(1)
            item['msg'] = check_match.group(1)
            item['file'] = file_match.group(1)
            item['line'] = int(file_match.group(2))
    return '%s:%d: %s: %s\n' % (fname, line, msg_type, msg)
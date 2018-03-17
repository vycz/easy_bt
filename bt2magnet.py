import libtorrent as bt


def bt2magnet(f):
    info = bt.torrent_info(f)
    print("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))
    return "magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name())

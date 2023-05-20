#!/bin/bash
nmcli connection import type openvpn file team-008.openvpn
nmcli connection modify team-008 ipv4.never-default true ipv6.never-default true
nmcli connection up team-008

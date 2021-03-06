# -*- coding: utf-8 -*-

class DiagramModel(object):
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes

    # ----------------------------------------------------------------------
    def __init__(self):
        self.last_id = 1  # first block is n1, increments to each new block
        self.blocks = {}  # GUI blocks
        self.connectors = []
        self.comments = []
        self.code_template = None

        self.zoom = 1.0  # pixels per unit
        self.file_name = "Untitled"
        self.modified = False
        self.language = None
        self.undo_stack = []
        self.redo_stack = []
        self.authors = []

    # ----------------------------------------------------------------------
    @property
    def patch_name(self):
        name = self.file_name
        if "/" in name:
            name = name.split("/").pop()
            name = name.split(".")[0]
        return name

    # ----------------------------------------------------------------------
    def __str__(self):
        return str(self.patch_name)

# ----------------------------------------------------------------------

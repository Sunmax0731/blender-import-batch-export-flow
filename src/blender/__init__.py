bl_info = {
    "name": "取り込み・バッチ処理・出力フロー",
    "author": "Sunmax0731",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "category": "System",
}

import bpy

class SUNMAX_PT_alpha_panel(bpy.types.Panel):
    bl_label = "取り込み・バッチ処理・出力フロー"
    bl_idname = "SUNMAX_PT_blender_import_batch_export_flow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sunmax"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Closed alpha validation panel")
        layout.label(text="Blenderバッチ入出力")

classes = (SUNMAX_PT_alpha_panel,)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


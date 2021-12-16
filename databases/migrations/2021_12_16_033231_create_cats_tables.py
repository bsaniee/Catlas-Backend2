"""CreateCatsTables Migration."""

from masoniteorm.migrations import Migration


class CreateCatsTables(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("cats") as table:
            table.increments("id")

            table.timestamps()
            table.string("name")
            table.string("color")
            table.string("breed")
            table.string("image")
            table.string("description")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("cats")
